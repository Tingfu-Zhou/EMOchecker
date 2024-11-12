You will be performing sentiment analysis based on a scene description and conversation text. Your task is to interpret the speaker's emotions from the provided information and classify them into a single emotion category.

Assume that the image is the scene where the user is having a conversation, and the person in the picture is the user. Text is the content of user conversations. You need to analyze user sentiment according to the following steps.

1. Examine the scene description: Carefully consider the scene description. Look for indicators of emotion such as facial expressions, body language, and environmental factors that might influence the speaker's emotional state.

2. Examine the conversation text: Examine the conversation text for words, phrases, or tone that suggest the speaker's emotional state. Pay attention to the content of what is being said and how it is expressed.

3. Combine your analysis: Integrate your observations from both the visual and textual cues to form a comprehensive understanding of the speaker's emotional state.

4. Classify the emotion: Based on your analysis, determine the most prominent emotion expressed. Choose from the following categories:
   - joy
   - sadness
   - anger
   - fear
   - surprise
   - disgust
   - neutral

Output your final emotion classification as a single word, without any additional explanation or justification. For example, if you determine the speaker is expressing happiness, your entire output should be:

joy

Remember, you are only to output the emotion category. Do not provide any additional commentary, explanation, or answer to any other questions.

------------------------------------------
You will be performing sentiment analysis based on a scene description and conversation text. Your task is to interpret the speaker's emotions from the provided information and classify them into a single emotion category.

Assume that the image is the scene where the user is having a conversation, and the person in the picture is the user. Text is the content of user conversations. You need to analyze user sentiment according to the following steps.

First, examine the scene description:
<image_description>
{{IMAGE_DESCRIPTION}}
</image_description>

Next, read the conversation text:
<conversation_text>
{{CONVERSATION_TEXT}}
</conversation_text>

To analyze the sentiment:

1. Visual cues: Carefully consider the scene description. Look for indicators of emotion such as facial expressions, body language, and environmental factors that might influence the speaker's emotional state.

2. Textual cues: Examine the conversation text for words, phrases, or tone that suggest the speaker's emotional state. Pay attention to the content of what is being said and how it is expressed.

3. Combine your analysis: Integrate your observations from both the visual and textual cues to form a comprehensive understanding of the speaker's emotional state.

4. Classify the emotion: Based on your analysis, determine the most prominent emotion expressed. Choose from the following categories:
   - joy
   - sadness
   - anger
   - fear
   - surprise
   - disgust
   - neutral

Output your final emotion classification as a single word, without any additional explanation or justification. For example, if you determine the speaker is expressing happiness, your entire output should be:

<emotion>joy</emotion>

Remember, you are only to output the emotion category. Do not provide any additional commentary, explanation, or answer to any other questions.



----old:
# assistant: EMOchecker
from openai import OpenAI
client = OpenAI()


assistant = client.beta.assistants.create(
  name="EMOchecker",
  instructions="You are a sentiment analysis assistant and you need to analyze the user's emotions. Keep your answers brief.\
    Sentiment analysis is divided into two steps. The first step is to determine which category the input belongs to based on its characteristics.\
        The second step is to perform corresponding prompt engineering based on the corresponding category.\
          Step 1: You need to help me complete the sentiment analysis. I need you to think in the following way, analyze the input information, and classify it into one of the following five categories based on the characteristics of the input information.\
            Category 1: Pattern Reframing: There are many low-level patterns in the input text, it can be extrapolated by finding low-level patterns. For example, several low-level patterns such as 'what might happen?', 'would…?', 'why is it possible?', 'what might it lead to' appear in the input text.\
              Category 2: Itemizing Reframing: Input text has long paragraphs stating multiple requirements. Although the text has the potential for a bulleted list, it has not been transformed into an actual list of items. For example, the iupt text is 'Follow the instructions to produce output with the given context word. Do A. Do B. Do not C'\
                Category 3: Decomposition Reframing: Input text contains tasks with implicit multi-step reasoning\
                  Category 4: Restraining Reframing: This is the most common and general case, and it is appropriate to add some constraints to avoid when the task definition deviates from its pre-training goal.\
                    Step 2: perform corresponding prompt engineering based on the corresponding category.\
                      Prompting for Category 1: Find low-level patterns among the devset examples and extrapolate those by adding similar patterns. For example, in the case that input text contains several low-level patterns like 'what might happen?', 'would…?', 'why is it possible?', 'what might it lead to', focus on these pattern and similar phrases in your answer based on the input context\
                        Prompting for Category 2: Turn long descriptions into bulleted lists of several statements. Additionally, turn negative statements to positive ones. For example, reformulate 'don't create questions which are not answerable from the paragraph' into 'create questions which are answerable from the paragraph'.\
                          Prompting for Category 3: Decompose a task into multiple different sub-tasks which can be executed either sequentially or in parallel and hence, make them relatively easier for models. Using the idea of Chain of Thought, that is, reasoning step by step.\
                            Prompting for Category 4: Add the following hint to the original input:  Are there Opinion texts in the input text? If so, is it positive or negative? Are there slang, irony, sarcasm, abbreviations, and emoticons in the text? Is there facial information in the video message? If so, is this facial information positive or negative? Is there a smile in the visual message? Is there eye contact in facial information?",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
  temperature=0.2,
)

print(assistant)

