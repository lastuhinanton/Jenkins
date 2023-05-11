"""
    This script push the status of the pipeline to the Telegram bot
"""

import jenkins
from jenkinsapi.jenkins import Jenkins

def notify_to_bot(token_id, user_id):
    print(token_id, user_id)

if __name__ == "__main__":
    jenkins_url = 'http://localhost:8080'
    username = 'admin'
    password = 'admin'
    server = Jenkins(jenkins_url, username=username, password=password)
    credential_id = 'token_id'
    creds = server.credentials(credential_id)
    print(creds.get_secret().get_plain_text())
