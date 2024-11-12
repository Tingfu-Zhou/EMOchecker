from openai import OpenAI

# 初始化OpenAI客户端
client = OpenAI()

# 获取所有文件列表
response = client.files.list()

# 获取文件ID
file_ids = [file.id for file in response.data]  # 访问 .data 属性

# 批量删除所有文件
for file_id in file_ids:
    delete_response = client.files.delete(file_id)
    print(f"Deleted file with ID {file_id}")

print("All files have been deleted.")

