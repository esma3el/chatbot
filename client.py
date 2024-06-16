import requests

msg = 'hello mr ismail mosa ibrahim'
url = "http://localhost:3300/get_msg"

payload = f'{{"data": "{msg}" }}'
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
print(response.status_code)
print(response.content)