import json
from .jsonify import write_json


def auth(update, context, filename):
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
    existing_id = []
    with open(filename, 'r') as f:
        file_data = json.load(f)
        temp_file_data = file_data["user_details"]
        for i in temp_file_data:
            if i['id'] == json_data.id:
                existing_id.append(i['id'])
        if json_data.id not in existing_id:
            write_json(formatted_data, filename)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=f"Hi {json_data.first_name}\nYou are Sucessfully Registered to AyImageBot Service.\nUse /get `<your-search>` to find a image.\nThank You")
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=f"Hi {json_data.first_name}\nWelcome Back again\nYou are Already Registered to AyImageBot Service.\nUse /get `<your-search>` to find a image.\nThank You")
