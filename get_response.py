import os
import openai
from get_config import get_org_config_summary

openai.api_key = os.environ['CHATGPT_KEY']  #chatgpt auth

def chat_completion(prompt):
    message = [{"role": "system", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
    )

    answer = response.choices[0].message.content
    return answer

def get_analysis():
    #fetch config
    summary_prompt = get_org_config_summary()

    #example prompt
    prompt = f"Here is an AWS organization config summary: {summary_prompt}. Please analyze this configuration and make some recommendations based off of it that will help enhance the overall security of this AWS org. These recommendations can be as specific or as general as need be. The overall goal is to enhance the AWS org's security."

    response = chat_completion(prompt)
    print(f"\n\nConfig Analysis: {response}\n\n")