import pandas as pd
import re
import time  # 导入time模块
from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI()

# 实验数量
max_experiments = 200

# 记录程序开始时间
start_time = time.time()

# 读取 CSV 文件
uploaded_file_ids_path = "C:\\Users\\tingf\\Desktop\\uploaded_file_ids.csv"
train_sent_emo_path = "C:\\Users\\tingf\\Desktop\\train_sent_emo.csv"


# 加载图片ID、文本信息和情感标签
file_ids_df = pd.read_csv(uploaded_file_ids_path)
texts_df = pd.read_csv(train_sent_emo_path)

# 确保两个数据框按顺序一致
file_ids = file_ids_df['File ID'][:max_experiments]  # 只读取前 100 行
utterances = texts_df['Utterance'][:max_experiments]  # 只读取前 100 行
sentiments = texts_df['Emotion'][:max_experiments]  # 获取前 100 行对应的情感标签

# 统计匹配正确的次数
correct_matches = 0

# 函数：清理文本，移除不必要的字符
def clean_text(text):
    # 去掉引号和前后空格
    return re.sub(r'[\'"]', '', text.strip().lower())

# 遍历每个文件ID和文本信息，构造并发送API请求
for file_id, utterance, sentiment in zip(file_ids, utterances, sentiments):
    # 创建一个对话线程，并包含图像引用和对应的文本
    thread = client.beta.threads.create(
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": utterance  # 使用文本
            },
            {
              "type": "image_file",
              "image_file": {"file_id": file_id}  # 使用图片ID
            },
          ],
        }
      ]
    )

    # 执行对话线程
    run = client.beta.threads.runs.create_and_poll(
      thread_id=thread.id,
      assistant_id='asst_7tpXkNQ3qjRlbOLGwkZibYtq',  # 请替换为实际的 assistant ID
      instructions="Note: The case I will send you next is to test the prompt (Assistant). Classify emotions into the following categories ['neutral' 'surprise' 'fear' 'sadness' 'joy' 'disgust' 'anger']. You only need to classify emotions and output the corresponding categories. You don't need to answer anything else. For example, If you judge that the character in the dialogue is happy based on the above method, you only need to output 'joy'."
    )

    # 检查对话状态并获取消息
    if run.status == 'completed':
        # 获取返回的消息
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        # 提取assistant的最后一条message中的content的value字段
        last_message_content = None
        for message in messages:
            if message.role == 'assistant':  # 只考虑 assistant 的回复
                for block in message.content:
                    if block.type == 'text':
                        last_message_content = block.text.value
                        break
                if last_message_content:
                    break

        # 清理last_message_content和sentiment，进行对比
        cleaned_message = clean_text(last_message_content) if last_message_content else None
        cleaned_sentiment = clean_text(sentiment)

        # 对比清理后的 message 和 Sentiment
        if cleaned_message and cleaned_message == cleaned_sentiment:
            correct_matches += 1
            print(f"Correct match for file {file_id}: {cleaned_message} == {cleaned_sentiment}")
        else:
            print(f"No match for file {file_id}: {cleaned_message} != {cleaned_sentiment}")
    else:
        print(f"Thread for file {file_id} is still {run.status}")


# 记录程序结束时间
end_time = time.time()

# 输出匹配正确的数量
print(f"Total correct matches: {correct_matches}")

# 输出程序运行的总时间
print(f"Total execution time: {end_time - start_time:.2f} seconds")
