"""
    This script push the status of the pipeline to the Telegram bot
"""

import sys
import requests

# TOKEN = sys.argv[1]
# CHAT_ID = sys.argv[2]
# RESULT = sys.argv[3]
# URL = sys.argv[4]
# NUMBER = sys.argv[5]
# NAME = sys.argv[6]

def notify_status_stage_to_bot(arrguments):
    TOKEN = arrguments[2]
    CHAT_ID = arrguments[3]
    RESULT = arrguments[4]
    URL = arrguments[5]
    NUMBER = arrguments[6]
    NAME = arrguments[7]
    SMILE= "✅" if RESULT == "SUCCESS" else "🚫"
    MESSAGE = f"""
========= Stage {NAME}  N=>{NUMBER}
Result: {SMILE}{RESULT}{SMILE} 
Link: {URL}
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
    requests.get(url).json()

if __name__ == "__main__":
    arrguments = sys.argv
    if arrguments[1] == "STAGE":
        notify_status_stage_to_bot(arrguments)
    elif arrguments[1] == "SUMMARY":
        pass