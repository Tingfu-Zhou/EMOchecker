from openai import OpenAI
client = OpenAI()

assistant = client.beta.assistants.create(
  name="EMOchecker",
  instructions="You are a sentiment analysis assistant and you need to analyze the user's emotions. Keep your answers brief.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)