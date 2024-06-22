from green_api import send_message
from flask import Flask ,request,Response
from waitress import serve

c1="0943ec77cfca5d75c8e91d1495666da6a8731378e9a680c04035dc066f628070"
c2="94010ef1a494e4975900bb6406cbd0e23e8300b5661ceb27b671e5fb449ef71d"
KEYS = [c1,c2]


app = Flask(__name__)

@app.post("/bot/160ae567-a19e-442c-9c54-1954f3c968e1")
def chatbot_route():
    key = request.headers.get("Chat-Key")
    if key not in KEYS:
        return Response("Error : UNAUTHORIZED ACCESS\n",status=401)
    msg = request.json
    
    send_message(msg)
    return Response("success.",status=200)

if __name__ == "__main__":
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=3300)
