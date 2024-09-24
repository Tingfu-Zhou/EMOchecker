from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You need to help me complete the sentiment analysis. You need to judge the user's emotion based on the input.\
                hint: Are there Opinion texts in the input text? If so, is it positive or negative? Are there slang, irony, sarcasm, abbreviations,\
                and emoticons in the text? Is there facial information in the video message? If so, is this facial information positive or negative? \
                Is there a smile in the visual message? Is there eye contact in facial information? Keep your answers brief."
        },
        {
            "role": "user",
            "content": "I really want to watch it again. What do you think of this movie?"
        }
    ],
    temperature=0.8,
    max_tokens=64,
    top_p=1
)


print(response.choices[0].message.content)
