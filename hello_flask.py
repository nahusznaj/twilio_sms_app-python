from flask import Flask

#app instance of Flask
app = Flask(__name__)

#decorator -- instructs flask to run the view function and uses the return to respond to the client when client hits the endpoint
@app.route('/hello-endpoint')
def view_function():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
