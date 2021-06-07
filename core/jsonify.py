import json

# Function to Add user to JSON


def write_json(new_data, filename):
    with open(filename, 'r') as f:
        file_data = json.load(f)
        with open(filename, 'w') as file:
            temp = file_data["user_details"]
            temp.append(new_data)
            json.dump(file_data, file, indent=4)
