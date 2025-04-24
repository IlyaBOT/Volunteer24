import uuid
from database import UserDatabaseManager

db = UserDatabaseManager()

sessions = {}

def process_auth(part_name=None, email=None, password=None):
    db = UserDatabaseManager()
    users = db.read_all_users()

    for user in users:
        db_email = user._mapping['email']
        if db_email.lower().strip() == email.lower().strip():
            user_uid = str(uuid.uuid4())
            sessions[user_uid] = email  # Привязка UID к email
            return {"success": True, "uid": user_uid}

    return {"error": "Пользователь с указанным email не найден"}