"""
    This script push the status of the pipeline to the Telegram bot
"""

import sys

def notify_to_bot(token_id, user_id):
    print(token_id, user_id)

if __name__ == "__main__":
    print(sys.argv[1:])

