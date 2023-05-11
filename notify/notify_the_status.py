"""
    This script push the status of the pipeline to the Telegram bot
"""

import sys
import requests

def notify_to_bot(token_id, user_id):
    print(token_id, user_id)

if __name__ == "__main__":
    print(sys.argv[3])
    print(sys.argv[4])
    print(sys.argv[5])
    TOKEN = sys.argv[1]
    CHAT_ID = sys.argv[2]
    MESSAGE = """
        Hello word!
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
    requests.get(url).json()

