from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user','content':prompt}],
        temperature=0
    )
    return response.choices[0].message.content