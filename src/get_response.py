import os
import openai
from get_config import get_org_config_summary

def chat_completion(prompt):

    openai.api_key = os.environ['CHATGPT_KEY']  #chatgpt auth
    
    message = [{"role": "system", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
    )

    answer = response.choices[0].message.content
    return answer

def get_analysis(custom_prompt):
    #fetch config
    config_summary = get_org_config_summary()

    #prompt
    prompt = f"Here is an AWS organization config summary: {config_summary}. {custom_prompt}"

    response = chat_completion(prompt)
    print(f"\n\nConfig Analysis: {response}\n\n")