import telegram
import logging

import requests

from telegram.ext import Updater

token = '<put your token here>'
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    context.bot.send_message(
    	chat_id=update.effective_chat.id, 
    	text="I'm a bot, please talk to me!"
    )

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

from telegram.ext import MessageHandler, Filters

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(
    	chat_id=update.effective_chat.id, 
    	text=update.message.text
    )

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

def get(update: Update, context: CallbackContext):
	url = 'https://lenta.ru'
	resp = requests.get(url)
	text = resp.text[:20]
	print(text)
	context.bot.send_message(chat_id=update.effective_chat.id, text=text)

get_handler = CommandHandler('get', get)
dispatcher.add_handler(get_handler)

updater.start_polling()
