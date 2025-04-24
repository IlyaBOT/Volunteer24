# auth.py

def process_auth(part_name=None, email=None, password=None):
    # Тут можно делать что угодно: проверку, запись в базу, логирование и т.д.
    if part_name:
        return f"{part_name} ({email}) {password}"
    else:
        return f"{email} {password}"
