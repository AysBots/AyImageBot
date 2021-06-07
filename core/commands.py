from telegram.ext import CallbackContext
from telegram import Update
from .urls import get_image, get_url
from .jsonify import write_json

DATAFILE = '../data.json'

# Command Functions
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    print(update.effective_chat)

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def unknown_text(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I don't know that.")

def get(update, context):
    msg = update.message.text
    msg = msg.split(" ")
    msg.pop(0)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Sending Image.\nPlease Wait...")
    update.message.reply_photo(get_image(get_url(search=msg)))

