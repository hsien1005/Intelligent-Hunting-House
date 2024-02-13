from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage, MessageEvent, TextMessage, ImageSendMessage


line_bot_api = LineBotApi('url')


handler = WebhookHandler('id')
def send_message(name,money,zone,img_list):
    try:
        user_id = "id"   
        message_text = name
        image_url = img_list[0]  
        link_url = "https://rent.591.com.tw/"  
        message = "名稱: "+message_text+" \n價錢: "+money+"元 \n地區: "+zone +" \n網站: "+ link_url
        text_message = TextSendMessage(text=message)
        image_message = ImageSendMessage(original_content_url=image_url, preview_image_url=image_url)

        line_bot_api.push_message(user_id, [text_message, image_message])

        return "Message sent to user {}".format(user_id)
    except Exception as e:
        return "Line Bot API Error: {}".format(e)

    
def webhook():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

