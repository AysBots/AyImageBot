from telegram.ext import CallbackContext
from telegram import Update, ParseMode
from .urls import get_image, get_final_image, fetch_unsplash_api
from .userauth import auth, update_requests
from .variables import DATAFILE, UNSPLASH_CLIENT_KEY, SEARCHDATAFILE
import os
from .snips import searchdata


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    auth(update=update, context=context, filename=DATAFILE, silent=False)


def help_cmd(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Help\n\nHi there! My name is AyImageBot. I am a free image sending bot.\n\nHelpful commands:\n- /get: To send a random image.\n- /get <search-image>: To send the image you want.\n- /start: To starts me. You've probably already used this.\n- /help: To sends this message; I'll tell you more about myself!\n\nImage search example:\n/get dog\n/get cat\nor anything with /get\n\nRemember:\nKeep the image search query as precise as possible. Try avoiding spaces.\nExample:\n/get Taj Mahal ❌\n/get tajmahal ✅\n\nIf you have any bugs or questions on how to use me, have a look at my repo website (in bio) or, head over to @AysBots group.")
    auth(update=update, context=context, filename=DATAFILE, silent=True)


def about(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi, I'm AyImageBot👋\n\nI'm part of an opensource organisation i.e., @AysBots.\nI can send you free high quality images just by using a simple /get command\nFor list of other commands use /help\n\nFeel free to use me anytime, not anywhere because currenty I'm available only on Telegram.\n\nIf you are a developer and wish to contribute in my development, then you can contibute on github.com/AysBots/AyImageBot.\n\nMy other family members are coming soon.\n\nSo, Stay Tuned 💓")
    auth(update=update, context=context, filename=DATAFILE, silent=True)


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
    searchdata(text=msg, filename=SEARCHDATAFILE)
    if msg == "" or msg == "/get" or msg == "/get ":
        msg = "random"
    else:
        msg = msg.split(" ")[1:]
        msg = "+".join(msg)
    image_name = str(update.effective_user.id) + '.jpeg'
    if update.effective_chat.type == "private":
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"Sending Image.\nPlease Wait...")
        try:
            caption = get_final_image(CLIENT_KEY=UNSPLASH_CLIENT_KEY,
                                        query=msg, filename=image_name)
            context.bot.sendPhoto(
                chat_id=update.effective_chat.id, photo=open(image_name, 'rb'), caption=caption, parse_mode=ParseMode.HTML) #
            # update.message.reply_photo(open('image.jpeg','rb'))
            os.remove(image_name)
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Sorry, I not found any match.\nPlease, try again with another key word.\n Use /help if problem continues")
        auth(update=update, context=context, filename=DATAFILE, silent=True)
        update_requests(update=update, filename=DATAFILE)
