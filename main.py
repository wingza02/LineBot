from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

api = Flask(__name__)

line_bot_api = LineBotApi('k8K8L+Xs4X+5mJTSl7eML5P2IZiizAU0FHD0oCmCjiXcy8dacW+V3I2Z2xUbRgCByBMjjq6Q0kww8k3O6Xfmw5TVr3hBwejwMjoeuv3ase9N++hRotp1qALa/OnmTCL0q3K+tARmmvoQWjdsaXgGGwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('07bf6b330c9a90298323b85b44650ce0')

@api.route("/")
def hello():
    return "Hello World!"

@api.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    api.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.source))


if __name__ == "__main__":
    api.run()