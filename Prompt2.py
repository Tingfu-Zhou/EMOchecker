import openai

openai.api_key = 'API key'

# the input text
text = "text content"

# chain of thought(prompt)
prompt = f"""
步骤一：分析文本内容
文本："{text}"

步骤二：识别关键动作

步骤三：类型匹配：
1. Pattern reframing：没有提及通过发现低级模式来推广。
2. Itemizing reframing：虽然文本有列表化的潜力，但并没有转化为实际的项目列表。
3. Decomposition reframing：文本将一个大任务（例如重新设计界面）分解为多个可以同时或顺序完成的子任务，符合这一点。
4. Restraining reframing：没有附加具体约束条件。
5. Specialization reframing：没有专门描述具体的低级任务或省略通用语句。

步骤四：基于以上分析，得出结论：
"""

# using API to generate the text
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=150
)

print(response.choices[0].text.strip())
