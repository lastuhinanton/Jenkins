"""
    This script push the status of the pipeline to the Telegram bot
"""

import sys
import requests

def notify_to_bot(token_id, user_id):
    print(token_id, user_id)

if __name__ == "__main__":
    TOKEN = sys.argv[1]
    CHAT_ID = sys.argv[2]
    RESULT = sys.argv[3]
    URL = sys.argv[4]
    NUMBER = sys.argv[5]
    MESSAGE = """
        Hello word!
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
    requests.get(url).json()

