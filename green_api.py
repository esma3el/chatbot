import os
import requests
from dotenv import load_dotenv

load_dotenv()

CHATID_PHONE = os.environ.get("CHATID_PHONE")
URL = os.environ.get("URL")
CONTENT_TYPE = os.environ.get("CONTENT_TYPE")

def send_message(msg):    
    payload = f'{{"chatId": "{CHATID_PHONE}@c.us","message": "{msg}" }}'
    headers = {'Content-Type': CONTENT_TYPE}
    response = requests.request("POST", URL, headers=headers, data = payload)
    return response
