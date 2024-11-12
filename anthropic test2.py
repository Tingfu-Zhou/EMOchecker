import os
import base64
import anthropic
import pandas as pd
import re
import time  # 导入time模块

# 初始化Anthropic客户端
client = anthropic.Anthropic()

# 记录程序开始时间
start_time = time.time()

# 实验数量
max_experiments = 200

# 本地图片文件夹路径
folder_path = "C:\\Users\\tingf\\Desktop\\extracted_middle_frames"

# 获取文件夹中的所有图片文件路径
file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.jpg', '.png', '.jpeg'))]

# 读取 CSV 文件
uploaded_file_ids_path = "C:\\Users\\tingf\\Desktop\\uploaded_file_ids.csv"
train_sent_emo_path = "C:\\Users\\tingf\\Desktop\\train_sent_emo.csv"

# 文本信息和情感标签
texts_df = pd.read_csv(train_sent_emo_path)

# 确保两个数据框按顺序一致
utterances = texts_df['Utterance'][:max_experiments]  # 只读取前 100 行
sentiments = texts_df['Emotion'][:max_experiments]  # 获取前 100 行对应的情感标签

# 统计匹配正确的次数
correct_matches = 0

# 函数：清理文本，移除不必要的字符
def clean_text(text):
    # 去掉引号和前后空格
    return re.sub(r'[\'"]', '', text.strip().lower())

# 遍历每个文件(并上传)和文本信息，构造并发送API请求
for file_path, utterance, sentiment in zip(file_paths, utterances, sentiments):
    # 读取图片并进行 Base64 编码
    with open(file_path, "rb") as image_file:
        image_data = base64.standard_b64encode(image_file.read()).decode("utf-8")
    
    # 获取图片的媒体类型
    if file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
        media_type = "image/jpeg"
    elif file_path.endswith(".png"):
        media_type = "image/png"
    else:
        continue  # 如果不是支持的格式，跳过
    
    # 构建消息并上传
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        temperature=0,
        system=""""
You will be performing sentiment analysis based on a scene description and conversation text. Your task is to interpret the speaker's emotions from the provided information and classify them into a single emotion category.

Assume that the image is the scene where the user is having a conversation, and the person in the picture is the user. Text is the content of user conversations. You need to analyze user sentiment according to the following steps.

1. Examine the scene description: Carefully consider the scene description. Look for indicators of emotion such as facial expressions, body language, and environmental factors that might influence the speaker's emotional state.

2. Examine the conversation text: Examine the conversation text for words, phrases, or tone that suggest the speaker's emotional state. Pay attention to the content of what is being said and how it is expressed.

3. Combine your analysis: Integrate your observations from both the visual and textual cues to form a comprehensive understanding of the speaker's emotional state.

4. Classify the emotion: Based on your analysis, determine the most prominent emotion expressed. Choose from the following categories:
   - joy
   - sadness
   - anger
   - fear
   - surprise
   - disgust
   - neutral

Output your final emotion classification as a single word, without any additional explanation or justification. For example, if you determine the speaker is expressing happiness, your entire output should be:

joy

Remember, you are only to output the emotion category. Do not provide any additional commentary, explanation, or answer to any other questions.""",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": utterance  # 使用文本
                    }
                ],
            }
        ],
    )

    output = message.content[0].text
    cleaned_sentiment = clean_text(sentiment)
    cleaned_output = clean_text(output)
    if cleaned_output and cleaned_output == cleaned_sentiment:
        correct_matches += 1
        print(f"Correct match for file {file_path}: {cleaned_output} == {cleaned_sentiment}")
    else:
        print(f"No match for file {file_path}: {cleaned_output} != {cleaned_sentiment}")

# 记录程序结束时间
end_time = time.time()

# 输出匹配正确的数量
print(f"Total correct matches: {correct_matches}")

# 输出程序运行的总时间
print(f"Total execution time: {end_time - start_time:.2f} seconds")

