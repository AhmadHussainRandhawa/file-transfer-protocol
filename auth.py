import json
from config import USERS_FILE


def load_users() -> dict:
    with open(USERS_FILE, "r") as file:
        return json.load(file)


def authenticate(username: str, password: str) -> bool:
    """
    Return True if the username/password pair is valid.
    """
    users = load_users()
    return users.get(username) == password