from openai import OpenAI
client = OpenAI()

assistant = client.beta.assistants.create(
  name="EMOchecker",
  instructions="You are a sentiment analysis assistant and you need to analyze the user's emotions. Keep your answers brief.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)

thread = client.beta.threads.create()
message1 = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I really want to watch it again. What do you think of this movie?"
)

