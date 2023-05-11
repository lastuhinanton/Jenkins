"""
    This script push the status of the pipeline to the Telegram bot
"""

import jenkins

def notify_to_bot(token_id, user_id):
    print(token_id, user_id)

if __name__ == "__main__":
    server = server = jenkins.Jenkins('http://localhost:8080', username='admin', password='admin')
    cred_token_id = server.get_credentials('token_id')
    print(cred_token_id['secret'].getPlainText())
