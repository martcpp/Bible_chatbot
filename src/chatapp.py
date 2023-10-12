from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from chatbot import generate_response


app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    print(incoming_msg)
    
    
    # msg = resp.message()
    response = generate_response(incoming_msg)
    print(response)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(response)
    
    return str(resp)
    
if  __name__ == "__main__":
    app.run()
