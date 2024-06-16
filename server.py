from green_api import send_message
from flask import Flask ,request,Response

app = Flask(__name__)

@app.get("/")
def index():
    return "hi"

@app.post("/get_msg")
def get_msg():
    msg = request.json
    print(msg['data'])
    send_message(msg=msg["data"])
    return Response("msg sent.",status=200)

if __name__ == "__main__":
    app.run(debug=True,port=3300)

