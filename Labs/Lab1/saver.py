import os
import json

def get_file_path(currency, date_str):
    os.makedirs(f"data/{currency}", exist_ok=True)
    return f"data/{currency}/{date_str}.json"

def already_downloaded(currency, date_str):
    return os.path.exists(get_file_path(currency, date_str))

def save_data(currency, date_str, json_data):
    path = get_file_path(currency, date_str)
    with open(path, "w") as f:
        json.dump(json_data, f, indent=2)