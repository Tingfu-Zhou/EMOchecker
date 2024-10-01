from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler

# 创建 OpenAI 客户端实例
client = OpenAI()

# 创建一个新线程
thread = client.beta.threads.create()

# 将消息添加到线程中
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I really want to watch it again. What do you think of this movie?"
)

# 定义事件处理类
class EventHandler(AssistantEventHandler):
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > {text}", end="", flush=True)

    @override
    def on_text_delta(self, delta, snapshot):
        print(delta.value, end="", flush=True)

    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end="", flush=True)
            if delta.code_interpreter.outputs:
                print(f"\n\noutput >", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        print(f"\n{output.logs}", flush=True)

# 使用stream SDK helper和EventHandler类创建Run并流式传输响应
with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id='asst_GCpx8sdV99bkxkHmDXe7FUyM',  # 使用直接 assistant_id
    instructions="This is a sentiment analysis test",
    event_handler=EventHandler(),
) as stream:
    stream.until_done()

