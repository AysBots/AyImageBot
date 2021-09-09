import dotenv, os

# TELEGRAM BOT API KEY
try:
    dotenv.load_dotenv()
    AYIMAGEBOT_API_KEY = os.getenv("AYIMAGEBOT_API_KEY")
except:
    AYIMAGEBOT_API_KEY = os.environ.get("AYIMAGEBOT_API_KEY")

# GET SERVER NAME
try:
    dotenv.load_dotenv()
    SERVER_NAME = os.getenv("SERVER_NAME")
except:
    SERVER_NAME = os.environ.get("SERVER_NAME")


# UNSPLASH IMAGE API KEY
try:
    dotenv.load_dotenv()
    UNSPLASH_CLIENT_KEY = os.getenv("UNSPLASH_CLIENT_KEY")
except:
    UNSPLASH_CLIENT_KEY = os.environ.get("UNSPLASH_CLIENT_KEY")

# GET PORT
PORT = int(os.environ.get('PORT', '5000'))
