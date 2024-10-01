from openai import OpenAI
client = OpenAI()

response = client.files.list()
print(response)

# her id = file-4g6VUAA9EgPnvXAlWVg9Y7Pg
