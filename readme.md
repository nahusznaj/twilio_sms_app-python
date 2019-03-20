# Create a Twilio SMS app with Flask

In this tutorial I'll walk you through the steps to create a simple but fun app with Twilio that sends quotes and cat photos by SMS/MMS. 

# Set up

These instructions are for Python3. Some steps may be different for versions earlier than 3.4 but the idea is the same.

1.  Check if you have python3 installed. Open a terminal and run:

    ```
    $ python3
    ```

    You should see the python prompt:


    ```
    $ python3
    Python 3.7.1 (default, Dec 14 2018, 13:28:58)
    [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    ```

    Exit python by running `exit()`.

    If this didn't work, you may not have python3 installed. Visit: https://www.python.org/downloads/ and follow the installation instructions for the latest version. I use [Anaconda](https://www.anaconda.com/).


2. Now, let's create a `virtual environment`. Using virtual environments is not mandatory, but it's good practice. It will keep your projects working despite future upgrades that may bring conflicts. (Note: For python with version earlier than 3.4 the instructions will be different, you can find instructions in google or stackoverflow.)

    1. *Tip*: create the virtual environemnt in the root project folder to keep things tidy. Let's first create a project folder:

        ```
        $ mkdir my_twilio_flask_app
        $ cd my_twilio_flask_app
        ```

    2. Create the virtual environment with a name of your choice, I put `twilio_app_venv`:

        ```
        $ python3 -m venv twilio_app_venv
        ```
        You'll find a `twilio_app_venv` folder within your project folder. Now activate the virtual environment:

        ```
        $ source twilio_app_venv/bin/activate
        ```

        If this worked, you'll see the terminal prompt a bit different: now it should display the virtual environment as in:

        ```
        (twilio_app_venv) Macbook:my_twilio_flask_app yourusername$ _
        ```


4. Check if you have `flask` installed:

    Run `import flask` in your python console:

    ```
    $ python3
    Python 3.7.1 (default, Dec 14 2018, 13:28:58)
    [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import flask
    >>>
    ```

    Unless there's an error, you're good to go. Run `exit()` to return to the terminal. 
    
    Otherwise, exit back to the the terminal and install `flask`:

    ```
    $ pip3 install flask
    ```


5. Install [Twilio's Software Development Kit (SDK)](https://www.twilio.com/docs/libraries/python#install-the-library):

    When a message comes in to the Twilio number, Twilio will make a POST request to our app's URL specified by us in the configuration to that Twilio's phone number. In order to respond to that POST request appropiately, we will use Twilio's helper library. Basically, our app will need to access some information from the incoming message (such as the body of the SMS), and depending on what the incoming messsage says, `return` with a response by generating Twiml (more on this below). So, let's install Twilio's SDK:

    ```
    $ pip3 install twilio
    ```

6. To close the circle, we need a Twilio phone number, which you can buy with credit with you sign up to Twilio.

    Get a Twilio account [here.](https://www.twilio.com/try-twilio)

    Buy a phone number (I would use a US mobile number, since Ireland numbers do not include all the functionalities that we need :( ).

    Once that's done, you can run the app, expose it with a webhook tunnel like ngrok, and add the url to the webhook for when "a message comes in" in your Twilio phone number configuration.
    
    **Getting help with Twilio**

    If you need help installing or using Twilio, please check the [Twilio Support Help Center](https://support.twilio.com) first, and [file a support ticket](https://twilio.com/help/contact) if you don't find an answer to your question.

    

## You're all set!

You can now use the python script in the repo and run it!

```
$ python3 FILE.py
```

## Set up a public URL and configure your Twilio number

Follow the instructions in [ngrok](https://ngrok.com/) to install it and to expose your local development machine to the internet. You'll have a public accessible URL, which tha Twilio can access. Use that URL in your Twilio phone number configuration for the field "message comes in".

If you find difficulties here, check out this [tutorial](https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python). And there's more info below. 

For instance, if you run the app and it's listening on port 5000:

```
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 175-012-267
 ```

 You can open a tunnel to public internet with ngrok by:

 ```
 ngrok http 5000
 ```

 You'll find the ngrok debugger and the `Forwarding` URL, something like `http://[something].ngrok.io` will be publicly accessible. Then, the webhook for "a message comes in" in your Twilio number will be the URL `http://[something].ngrok.io/sms`.  Note that the `/sms` route was set by us in the `.py` app file!





## More info about Twilio:

[Twilio's Youtube channel](https://www.youtube.com/channel/UCWh3G9LZmZ3q_xWOyPpn8ag)

In particular: [How to Send and Receive SMS Using Python](https://www.youtube.com/watch?v=knxlmCVFAZI)

Explore [Twilio's Docs](https://www.twilio.com/docs/):

[Send SMS and MMS with Python](https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python) 

[Receive and Reply to SMS and MMS Messages in Python](https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python)

[Twilio's python library in Github](https://github.com/twilio/twilio-python)

[Configuring Phone Numbers to Receive and Respond to SMS and MMS Messages](https://support.twilio.com/hc/en-us/articles/223136047-Configuring-Phone-Numbers-to-Receive-SMS-Messages)

## Want to learn more Twilio? Get a free T-shirt by playing the awesome [TwilioQuest](https://www.twilio.com/quest/welcome)!

# The APIs

I used these two APIs, you are encouraged to explore and use others to match your app design! 


For cat pictures (I used a GET HTTP request): https://thecatapi.com/

For quotes (I used a POST HTTP request):  http://forismatic.com/en/api/


# Twiml

Twiml is Twilio's XML language that tells Twilio what to do when you receive an incoming SMS.

You can write your own Twiml explictly in the view function's `return` or you can generate it by using the Twilio Language Helper Libraries (which we installed above!).

When your Twilio number receives an incoming SMS, it will make a synchronous HTTP POST  request to URL configured for that number. Twilio will expect to receive TwiML in response to that POST request. This is why we configure the app to return Twiml.

The POST request that Twilio sends to your app includes a number of parameters (if you configured a GET request, this will change accordingly), including the "From" and "To" numbers, the "Body" of the message. For a full list visit this [page](https://www.twilio.com/docs/sms/twiml#request-parameters).


### More on [Twiml.](https://www.twilio.com/docs/sms/twiml#what-is-twiml)

