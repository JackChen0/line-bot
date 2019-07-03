from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('zCky2QfMUFjwudA9P1YbErlEoF1t3JvXVD8l739SE78Rx/ruiIZVlAxMGIR96AiemCVSMY+xR86ikrtxUHAap8IjVcuOU7M1C76GbeLhpUtsLJuHDB8y559+VXjNp/bhGVa3e5PHERMDMIgt3JM2iQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('abc362257ffbeb84d24d162004a82be5')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    reply = 'Sorry'
    
    if msg in ['hi ','hi','Hi']:
        reply = 'hi'
        a = '11537'
        b = '52002738'
    elif msg == 'bye bye':
        reply = 'See you'
    
    sticker_message = StickerSendMessage(
    package_id=a,
    sticker_id=b)


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply),
        sticker_message)
        return

if __name__ == "__main__":
    app.run()