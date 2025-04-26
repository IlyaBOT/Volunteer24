import uuid
from database import UserDatabaseManager

db = UserDatabaseManager()

def process_auth(part_name=None, email=None, password=None):
    db = UserDatabaseManager()
    db.print_all_users()
    users = db.read_all_users()

    for user in users:
        db_email = user._mapping['email']
        if db_email.lower().strip() == email.lower().strip():
            print("✅ Найден!")
            return {
                "success": True,
                "uid": str(uuid.uuid4())
            }

    return {"error": "Пользователь с указанным email не найден"}