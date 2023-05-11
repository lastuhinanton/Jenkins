"""
    This script push the status of the pipeline to the Telegram bot
"""

import os
import sys
import requests

def notify_to_bot(token_id, user_id):
    print(token_id, user_id)

if __name__ == "__main__":
    print(sys.argv[1].split("___"))
    # TOKEN = ""
    # CHAT_ID = 
    # MESSAGE = """
    #     Hello word!
    # """
    # url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
    # print(requests.get(url).json())

