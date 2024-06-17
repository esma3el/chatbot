from green_api import send_message
from flask import Flask ,request,Response
from waitress import serve

app = Flask(__name__)

@app.post("/bot/160ae567-a19e-442c-9c54-1954f3c968e1")
def chatbot_route():
    msg = request.json
    response = send_message(msg)
    return Response("success.",status=200)

if __name__ == "__main__":
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=3300)
