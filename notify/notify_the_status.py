"""
    This script push the status of the pipeline to the Telegram bot
"""

import sys
import requests

def notify_to_bot(token_id, user_id):
    print(token_id, user_id)

# TOKEN = sys.argv[1]
# CHAT_ID = sys.argv[2]
# RESULT = sys.argv[3]
# URL = sys.argv[4]
# NUMBER = sys.argv[5]
# NAME = sys.argv[6]
if __name__ == "__main__":
    TOKEN = "5962502114:AAF4DI2thksqdSMeTe-3RIWesJADtb79Guk"
    CHAT_ID = "1190955043"
    RESULT = "SUCCESS"
    URL = "http://localhost:8080/job/cd_pipe/81/"
    NUMBER = "77"
    NAME = "Build"
    SMILE= "✅" if RESULT == "SUCCESS" else "🚫"
    MESSAGE = f"""
========= Stage {NAME}  N> {NUMBER}
Result: {SMILE}{RESULT}{SMILE} 
Link: {URL}
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
    requests.get(url).json()
