import os
import dotenv
import logging
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from core.commands import start, unknown, unknown_text, get
from api_loader import AYIMAGEBOT_API_KEY


# Initialize Bot Key
API_KEY = AYIMAGEBOT_API_KEY
print("[+] APIKEY LOADED.....")


# Initializing Logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
print("[+] LOGGER STARTED.....")


# Check for errors
def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# Initialize Updater & Dispatcher
updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher


# Syncing commands with functions
start_handler = CommandHandler('start', start)
get_handler = CommandHandler('get', get)
unknown_handler = MessageHandler(Filters.command, unknown)
unknown_text_handler = MessageHandler(Filters.text, unknown_text)


# Adding Handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_handler)
dispatcher.add_error_handler(error)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(unknown_text_handler)


# Starting Bot
updater.start_polling()
updater.idle()
