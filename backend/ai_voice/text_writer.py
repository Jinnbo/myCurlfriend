from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# print(os.getenv("OPENAI_API_KEY"))
# print(os.getenv("ELEVENLABS_API_KEY"))

client = OpenAI()

#File that uses GPT API to create the text that the Eleven API will read
def textWriter(text: str):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": text}
    ]
    )

    print(completion.choices[0].message.content)
    # return text
    return completion.choices[0].message.content
