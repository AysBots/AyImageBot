import os
import sys
import time
import dotenv
import logging
import datetime
from threading import Thread
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from core.commands import start, help_cmd, about, unknown, unknown_text, get
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


# Stopper
def stop():
    '''
    This function is used to stop code in a certain amount of time
    '''
    # Turning off few minutes before 24 hours to restart and update code.
    time.sleep(86220)
    logging.shutdown()
    os._exit(1)

# Main function
def main():
    # Initial1ize Updater & Dispatcher
    updater = Updater(token=API_KEY, use_context=True)
    dispatcher = updater.dispatcher


    # Syncing commands with functions
    start_handler = CommandHandler('start', start)
    about_handler = CommandHandler('about', about)
    help_handler = CommandHandler('help', help_cmd)
    get_handler = CommandHandler('get', get)
    unknown_handler = MessageHandler(Filters.command, unknown)
    unknown_text_handler = MessageHandler(Filters.text, unknown_text)


    # Adding Handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(get_handler)
    dispatcher.add_error_handler(error)
    dispatcher.add_handler(unknown_handler)
    dispatcher.add_handler(unknown_text_handler)

    # Running Threads
    t1 = Thread(target = updater.start_polling)
    t2 = Thread(target = stop)
    t1.start()
    t2.start()
    updater.idle()



if __name__ == "__main__":
    main()
