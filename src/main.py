import time
import sys
import threading
from get_response import get_analysis
from dotenv import load_dotenv


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
    loading_stop_flag = threading.Event()
    loading_thread = threading.Thread(target=loading_spinner, args=(loading_stop_flag,))
    loading_thread.start()

    #fetch config analysis
    get_analysis()

    loading_stop_flag.set()
    loading_thread.join()

if __name__ == "__main__":
    load_dotenv()
    main()

