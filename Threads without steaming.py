from openai import OpenAI
client = OpenAI()

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I really want to watch it again. What do you think of this movie?"
)

run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id='asst_GCpx8sdV99bkxkHmDXe7FUyM',
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
else:
  print(run.status)