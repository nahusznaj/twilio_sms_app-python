from flask import Flask, request, redirect
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
import requests 
import json

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    resp = MessagingResponse() #set up the twiml for response

    ## quote API request with Requests. I used a POST, this is explained in their website.
    
    r = requests.post('http://api.forismatic.com/api/1.0/', data = {'method':'getQuote', 'key':'457653', 'format':'json', 'lang':'en'})
    quote_response = json.loads(r.text)
    quote = quote_response['quoteText'] + ' ' + quote_response['quoteAuthor']
    
    ## the cat API!
    response_image = requests.get('https://api.thecatapi.com/v1/images/search')
    data_image = json.loads(response_image.content)
    image_url = data_image[0]['url']

    # with twilio, read the body of the incoming message in the body variable 
    body = request.values.get('Body', None) 

    if body == 'Yes' or body == 'yEs' or body == 'yeS' or body == 'yes' or body == 'YES':
        msg = resp.message(quote)
        msg.media(image_url)
        return str(resp)
    elif body == "No" or body == 'NO' or body == 'nO':
        resp.message("Oh... you said No!")
        return str(resp)
    else: 
        resp.message("Please say Yes or No")
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
