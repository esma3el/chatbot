import requests

def send_message(msg):
    url = "https://7103.api.greenapi.com/waInstance7103946502/sendMessage/c1c8c879bd8a409eb6122919c7ef6601b4d9e648c98646a585"

    payload = f'{{"chatId": "249908225563@c.us", "message": "{msg}" }}'
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))