from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI()

# 使用上一步获得的 `file_id`，而不是本地文件
file_id = 'file-4g6VUAA9EgPnvXAlWVg9Y7Pg'  # 请将其替换为上一步上传时返回的实际 `file_id`

# 创建一个对话线程，并包含图像引用
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "I really want to watch it again. What do you think of this movie?"
        },
        {
          "type": "image_file",
          "image_file": {"file_id": file_id}  # 使用 `file_id` 引用文件
        },
      ],
    }
  ]
)

# 执行对话线程
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id='asst_GCpx8sdV99bkxkHmDXe7FUyM',
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

# 检查对话状态并获取消息
if run.status == 'completed':
  messages = client.beta.threads.messages.list(thread_id=thread.id)
  print(messages)
else:
  print(run.status)
