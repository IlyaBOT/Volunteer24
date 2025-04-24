import uuid
from database import UserDatabaseManager

db = UserDatabaseManager()

def process_auth(part_name=None, email=None, password=None):
    db = UserDatabaseManager()
    users = db.read_all_users()
    found = False

    for user in users:
        db_email = user._mapping['email']  # Получаем поле из строки
        if db_email.lower() == email.lower():
            found = True
            break

    if not found:
        return {"error": "Пользователь с указанным email не найден"}

    import uuid
    user_uid = str(uuid.uuid4())
    print(f"✅ UID для {email}: {user_uid}")
    return {"success": True, "uid": user_uid}
