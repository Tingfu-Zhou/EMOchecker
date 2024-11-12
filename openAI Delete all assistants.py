from openai import OpenAI

# 初始化OpenAI客户端
client = OpenAI()

# 获取所有助理的列表
my_assistants = client.beta.assistants.list()

# 获取助理的ID
assistant_ids = [assistant.id for assistant in my_assistants.data]

# 批量删除所有助理
for assistant_id in assistant_ids:
    response = client.beta.assistants.delete(assistant_id)
    print(f"Deleted assistant with ID {assistant_id}")

print("All assistants have been deleted.")
