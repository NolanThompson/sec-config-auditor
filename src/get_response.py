import os
import openai
from get_config import get_org_config_summary


def chat_completion(prompt):
    openai.api_key = os.environ['CHATGPT_KEY']  # ChatGPT auth

    message = [{"role": "system", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
    )

    answer = response.choices[0].message.content
    return answer


def get_analysis(custom_prompt, cloud_provider):
    # fetch config
    config_summary = get_org_config_summary(cloud_provider)

    if config_summary is None:
        print("Failed to retrieve organization configuration summary.")
        return

    # prompt
    if cloud_provider == 'aws':
        prompt = f"Here is an AWS organization config summary: {config_summary}. {custom_prompt}"
    elif cloud_provider == 'azure':
        prompt = f"Here is an Azure organization config summary: {config_summary}. {custom_prompt}"
    else:
        print("Invalid cloud provider specified.")
        return

    response = chat_completion(prompt)
    print(f"\n\nConfig Analysis: {response}\n\n")