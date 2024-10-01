from openai import OpenAI
client = OpenAI()

file_path = "C:\\Users\\tingf\\Desktop\\her.jpg"
response = client.files.create(file=open(file_path, "rb"), purpose='vision')

print(response)

