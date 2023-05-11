"""
    This script push the status of the pipeline to the Telegram bot
"""

import sys
import requests

def notify_to_bot(token_id, user_id):
    print(token_id, user_id)

if __name__ == "__main__":
    info = sys.argv[1].split("___")
    TOKEN = info[0]
    CHAT_ID = info[1]
    MESSAGE = """
        Hello word!
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
    print(requests.get(url).json())

