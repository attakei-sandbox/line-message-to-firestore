#!/usr/bin/env python
import logging
import os
from bottle import Bottle, abort, request, run
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


app = Bottle()
handler = WebhookHandler(os.environ['LINE_CHANNEL_SECRET'])
line_bot_api = LineBotApi(os.environ['LINE_CHANNEL_TOKEN'])
logging.basicConfig(level=logging.DEBUG)


@app.route('/callback', method='POST')
def callback():
    body = request.body.read().decode()
    logging.debug(f'Request body: {body}')

    signature = request.headers.get('X-Line-Signature')
    logging.debug(f'Request signature: {signature}')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        logging.warn('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)
    except Error as err:
        logging.error(str(err))
        abort()
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


@app.route('/hello')
def hello():
    logging.debug('Requested hello')
    return "Hello World!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8080'))
    debug = bool(os.environ.get('DEBUG', False))
    run(app, host='0.0.0.0', port=port, debug=debug)
