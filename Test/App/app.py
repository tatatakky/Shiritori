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

line_bot_api = LineBotApi('oKhAwI/kG3dllrKoX6qJjFb3dddmzL1zNvmy1k5sbli14o0tPknWWUyVUnlih2jsXEcMXnzMcuhc2Km5GZePWGViDbdSwAUCiinAYTDIFtpAgBT1rLtlgeBKT9JE/WjMSFBpp1F3w3r7mwUubnrBKwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('febb4b1de5bbee2b405895f60acc4bb4')


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
