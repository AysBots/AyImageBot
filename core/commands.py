from telegram.ext import CallbackContext
from telegram import Update
from .urls import get_image, get_url_source_unsplash
from .userauth import auth, update_requests
from .variables import DATAFILE


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    auth(update=update, context=context, filename=DATAFILE, silent=False)


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")
    auth(update=update, context=context, filename=DATAFILE, silent=True)


def unknown_text(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I don't know that.")
    auth(update=update, context=context, filename=DATAFILE, silent=True)


def get(update, context):
    msg = update.message.text
    msg = msg.split(" ").pop(0)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Sending Image.\nPlease Wait...")
    update.message.reply_photo(get_image(get_url_source_unsplash(search=msg)))
    auth(update=update, context=context, filename=DATAFILE, silent=True)
    update_requests(update=update, filename=DATAFILE)
