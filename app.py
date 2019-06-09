from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])   #for getting twilio request and sending response to server 
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    sender=request.form.get('From')
    
    print(request.form)
    #print(msg)

    # Create reply
    resp = MessagingResponse()
    
    #resp.message("You said: {}".format(msg)).media('https://cdn.pixabay.com/photo/2018/10/30/16/06/water-lily-3784022__340.jpg')
    resp.message(fetch_reply(msg,sender))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)



