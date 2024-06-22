import os
import requests
from dotenv import load_dotenv

load_dotenv()

CHATID_PHONE = os.environ.get("CHATID_PHONE")
GREENAPIURL = os.environ.get("GREENAPIURL")

def send_message(msg):    
    payload = f'{{"chatId": "{CHATID_PHONE}@c.us","message": "{msg}" }}'
    print(GREENAPIURL)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", GREENAPIURL, headers=headers, data = payload)
    
    return response
