from openai import OpenAI
client = OpenAI()

response = client.beta.assistants.delete("asst_X9tcxpIoxPazqcO5CUhyQw17")
print(response)
