from tinydb import TinyDB, Query
from .snips import all_permit
import os


def auth(update, context, filename, silent: bool):
    json_data = update.effective_user
    formatted_data = {
        "id": json_data.id,
        "username": f"{json_data.username}",
        "first_name": f"{json_data.first_name}",
        "last_name": f"{json_data.last_name}",
        "is_bot": str(json_data.is_bot),
        "type": f"{update.effective_chat.type}",
        "requests": 0
    }
    if os.path.isfile(filename):
        pass
    else:
        open(filename, "a").close()
        try:
            all_permit(filename)
        except:
            pass
    db = TinyDB(filename, sort_keys=True, indent=2, separators=(',', ': '))
    db.default_table_name = "Users"
    Users = Query()
    if db.search(Users.id == json_data.id) == []:
        db.insert(formatted_data)
        if not silent:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=f"Hi {json_data.first_name}\nYou are Sucessfully Registered to AyImageBot Service.\nUse /get `<your-search>` to find a image.\nFor more info type /help\nThank You")
    else:
        if not silent:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=f"Hi {json_data.first_name}\nWelcome Back again\nYou are Already Registered to AyImageBot Service.\nUse /get `<your-search>` to find a image.\nFor more info type /help\nThank You")
        db.update({'username': json_data.username},
                  Users.id == json_data.id)
        db.update({'first_name': json_data.first_name},
                  Users.id == json_data.id)
        db.update({'last_name': json_data.last_name},
                  Users.id == json_data.id)


def update_requests(update, filename):
    json_data = update.effective_user
    db = TinyDB(filename, sort_keys=True, indent=2, separators=(',', ': '))
    db.default_table_name = "Users"
    Users = Query()
    old_requests = db.get(Users.id == json_data.id)['requests']
    db.update({'requests': old_requests+1},
              Users.id == json_data.id)
