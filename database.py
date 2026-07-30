import json
import os

DB_FILE = "users.json"


def load_users():
    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def add_user(user):
    users = load_users()

    user_id = str(user.id)

    if user_id not in users:
        users[user_id] = {
            "id": user.id,
            "name": user.first_name,
            "username": user.username,
        }
        save_users(users)
