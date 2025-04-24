import uuid
from database import UserDatabaseManager

db = UserDatabaseManager()

def process_auth(part_name=None, email=None, password=None):
    users = db.read_all_users()
    found = False

    for user in users:
        if user.email.lower() == email.lower():
            found = True
            break

    if not found:
        return {"error": "Пользователь с указанным email не найден"}

    # Генерируем UID
    user_uid = str(uuid.uuid4())

    # Ты можешь создать отдельную таблицу с UID, или просто пока вывести
    print(f"UID для {email}: {user_uid}")

    return {"success": True, "uid": user_uid}
