from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": "You need to help me complete the sentiment analysis. I need you to think in the following way, analyze the input information, and classify it into one of the following five categories based on the characteristics of the input information."
    },
    {
      "role": "system",
      "content": "Category 1: Pattern Reframing: There is no mention of extrapolating by finding low-level patterns.\
          Category 2: Itemizing Reframing: Although the text has the potential for a bulleted list, it has not been transformed into an actual list of items.\
          Category 3: Decomposition Reframing: The text decomposes a major task (redesigning the interface) into several subtasks that can be completed either sequentially or simultaneously, fitting this category.\
            Category 4: Restraining Reframing: There are no additional statements expressing constraints about the output generation.\
                Category 5: Specialization Reframing: It does not specifically describe low-level tasks or omit any repeated or generic statements."
    }
    {
      "role": "user",
      "content": "Artificial intelligence is a technology with great promise."
    }
  ],
  temperature=0.8,
  max_tokens=64,
  top_p=1
)