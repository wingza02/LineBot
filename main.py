from flask import Flask, request
api = Flask(__name__)

@api.route("/")
def hello():
    return "Hello World!"

@api.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        return 'OK'

if __name__ == "__main__":
    api.run()