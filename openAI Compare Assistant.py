# assistant: EMOchecker
from openai import OpenAI
client = OpenAI()


assistant = client.beta.assistants.create(
  name="EMOchecker",
  instructions="You are the control group.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
  temperature=0,
)

print(assistant)

