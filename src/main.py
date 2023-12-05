import time
import sys
import threading
from get_response import get_analysis
from dotenv import load_dotenv
import os


#loading animation
def loading_spinner(stop_flag):
    chars = ['-', '\\', '|', '/']
    delay = 0.1

    while not stop_flag.is_set():
        for char in chars:
            sys.stdout.write('\rAnalyzing Configuration ' + char)
            sys.stdout.flush()
            time.sleep(delay)

def main():
    # Get the prompt from command line argument
    cloud_provider = sys.argv[1] if len(sys.argv) > 1 else None
    custom_prompt = sys.argv[2] if len(sys.argv) > 2 else None

    # Check for required environment variables
    required_vars_aws = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_DEFAULT_REGION", "CHATGPT_KEY"]
    required_vars_azure = ["AZURE_SUBSCRIPTION_ID", "CHATGPT_KEY"]

    if cloud_provider == 'aws':
        missing_vars = [var for var in required_vars_aws if not os.getenv(var)]
    elif cloud_provider == 'azure':
        missing_vars = [var for var in required_vars_azure if not os.getenv(var)]
    else:
        print("Invalid cloud provider specified.")
        return

    if missing_vars:
        print(f"Missing environment variables: {', '.join(missing_vars)}. Please set them in your .env file.")
        return

    loading_stop_flag = threading.Event()
    loading_thread = threading.Thread(target=loading_spinner, args=(loading_stop_flag,))
    loading_thread.start()

    #fetch config analysis
    get_analysis(custom_prompt, cloud_provider)

    loading_stop_flag.set()
    loading_thread.join()

if __name__ == "__main__":
    load_dotenv()
    main()

