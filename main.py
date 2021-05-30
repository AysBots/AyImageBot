import requests, os, dotenv, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update


# Initialize Bot Key
dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")
print("[+] APIKEY LOADED.....")

# Initializing Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger= logging.getLogger(__name__)
print("[+] LOGGER STARTED.....")

# General Function
def get_image(url, print_url=False):
    '''
    Convert URL to original image link
    '''
    response = requests.get(url)
    if print_url:
        print(response.url)
    return response.url
url= r"https://source.unsplash.com/random"

# Command Functions
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def get(update, context):
    print(update.message.text)
    msg = update.message.text
    msg = msg.split(" ")
    msg.pop(0)
    # for i in msg:
    #     print(i)
    # print(f" this is {msg}")
    # update.message.reply_photo(get_image(url))


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# Initialize Updater & Dispatcher
updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher


# Syncing commands with functions
start_handler = CommandHandler('start', start)
start_handler = CommandHandler('get', get)
unknown_handler = MessageHandler(Filters.command, unknown)


# Adding Handlers
dispatcher.add_handler(start_handler)                
dispatcher.add_error_handler(error)
dispatcher.add_handler(unknown_handler)


# Starting Bot
updater.start_polling()
updater.idle()