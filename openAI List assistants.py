from openai import OpenAI
client = OpenAI()

my_assistants = client.beta.assistants.list()
print(my_assistants.data)
