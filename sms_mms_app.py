from flask import Flask, request, redirect
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
import requests 
import json

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    resp = MessagingResponse()

    # response = requests.get("https://favqs.com/api/qotd")
    # data = json.loads(response.content)           
    # daily_quote = data['quote']['body'] 
    r = requests.post('http://api.forismatic.com/api/1.0/', data = {'method':'getQuote', 'key':'457653', 'format':'json', 'lang':'en'})
    quote_response = json.loads(r.text)
    quote = quote_response['quoteText'] + ' ' + quote_response['quoteAuthor']
    
    response_image = requests.get('https://api.thecatapi.com/v1/images/search')
    data_image = json.loads(response_image.content)
    image_url = data_image[0]['url']
    #image_url = 'https://globintel.com/wp-content/uploads/2019/03/Seiichi-Miyake-780x405.jpg'

    body = request.values.get('Body', None)
    # from_number = request.values.get('From', None)
    # if from_number == my_number:

    if body == 'Yes' or body == 'yEs' or body == 'yeS' or body == 'yes' or body == 'YES':
        msg = resp.message(quote)
        msg.media(image_url)
        return str(resp)
        # return """<?xml version="1.0" encoding="UTF-8"?>
        # <Response>
        #     <Message>
        #         <Body>""" + quote + """</Body>
        #         <Media>""" + image_url + """ </Media>
        #     </Message>
        # </Response>"""
    elif body == "No" or body == 'NO' or body == 'nO':
        resp.message("Oh... you said No!")
        return str(resp)

        #return """<?xml version="1.0" encoding="UTF-8"?><Response><Sms> Oh... you said No!</Sms></Response>"""
    else: 
        return """<?xml version="1.0" encoding="UTF-8"?><Response><Sms>Please say Yes or No</Sms></Response>"""


if __name__ == "__main__":
    app.run(debug=True)