from flask import Flask, request, redirect
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
import requests 
import json

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    resp = MessagingResponse() #set up the twiml response
  
    # with twilio, read the body of the incoming message in the body variable 
    body = request.values.get('Body', None) 

    if body.strip().lower() == 'yes':
        ## make a resquest to quote API with Requests. See: http://forismatic.com/en/api/
        r = requests.post('http://api.forismatic.com/api/1.0/', data = {'method':'getQuote', 'key':'457653', 'format':'json', 'lang':'en'})
        quote_response = json.loads(r.text)
        quote = quote_response['quoteText'] + ' ' + quote_response['quoteAuthor']
        msg = resp.message(quote)
        return str(resp)
    elif body.strip().lower() == 'no':
        resp.message("Oh... you said No!")
        return str(resp)
    else: 
        resp.message("Please say Yes or No")
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
