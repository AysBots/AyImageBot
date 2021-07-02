from telegram.ext import CallbackContext
from telegram import Update
from .urls import get_image, get_final_image, fetch_unsplash_api
from .userauth import auth, update_requests
from .variables import DATAFILE, UNSPLASH_CLIENT_KEY
import os


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
    if msg == "" or msg == "/get" or msg == "/get ":
        msg = "random"
    else:
        msg = msg.split(" ")[1:]
        str1 = ""
        for i in msg:
            str1 = str1+i
        msg = str1
    image_name = str(update.effective_user.id) + '.jpeg'
    if update.effective_chat.type == "private":
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"Sending Image.\nPlease Wait...")
        try:
            get_final_image(CLIENT_KEY=UNSPLASH_CLIENT_KEY,
                            query=msg, filename=image_name)
            context.bot.sendPhoto(
                chat_id=update.effective_chat.id, photo=open(image_name, 'rb'))
            # update.message.reply_photo(open('image.jpeg','rb'))
            os.remove(image_name)
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Sorry, I am facing some problem.\nPlease try again.")
        auth(update=update, context=context, filename=DATAFILE, silent=True)
        update_requests(update=update, filename=DATAFILE)
        