from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from test import *

app = Flask(__name__)

line_bot_api = LineBotApi('cZlLzm3ERHan6bhmD6cFDNjmYyOfg8NSzK6Xl539TJHdOtrJrAKu8Y3dAdGlO5oSQNqd7m72aVeBvyObLh2EZjkvbhBWnPr7mWEroeMxYJrC3oOBBoqEvTxQpAdqLzZoUubkm6o+34J1sE3NA6Vu4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('16f8fa52cf8109c4d31ba733e28ed725')

#ジョンヨンの画像
# https://bebe.jpn.com/wp-content/uploads/2017/10/21984973_692873177550116_3197279010690170880_n-640x800.jpg

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        # TextSendMessage(text=event.message.text)
        TextSendMessage(text=Hello())
        )

if __name__ == "__main__":
    app.run()
