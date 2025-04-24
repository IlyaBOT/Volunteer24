import pandas as pd
from sqlalchemy import create_engine, Table, Column, String, Integer, MetaData
from sqlalchemy.sql import select

# Настройки подключения к БД (замени под себя)
DB_USER = 'dbuser'
DB_PASSWORD = 'IB2025IB'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'db_sport24'

# URL для подключения к PostgreSQL
database_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаём движок SQLAlchemy
engine = create_engine(database_url)

# Создание таблицы
metadata = MetaData()
users_table = Table('users', metadata,
    Column('full_name', String(255), primary_key=True),
    Column('inn', Integer),
    Column('phone', Integer),
    Column('email', String(255)),
    Column('birth_date', String(20)),
    Column('achievements', String(500))
)

metadata.create_all(engine)

# Загрузка CSV
csv_file = '../test_data.csv'
df = pd.read_csv(csv_file)

# Переименование колонок под SQL
df.columns = ['full_name', 'inn', 'phone', 'email', 'birth_date', 'achievements']

# Преобразование INN к числу (удаляем все нецифровые символы)
df['inn'] = df['inn'].astype(str).str.replace(r'\D', '', regex=True).astype('int64')

# Обработка телефона: +7 999 123-45-67 -> 79991234567
df['phone'] = df['phone'].astype(str)
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)  # удалить всё кроме цифр
df['phone'] = df['phone'].str.replace(r'^8', '7', regex=True)  # если номер начинается с 8, заменить на 7
df['phone'] = df['phone'].astype('int64')

# Загрузка в БД
df.to_sql('users', con=engine, if_exists='replace', index=False)

print("Данные успешно загружены в базу!")

# Чтение всех записей из базы и вывод
with engine.connect() as connection:
    result = connection.execute(select(users_table))
    all_users = result.fetchall()
    print("\nВсе записи в таблице users:")
    for user in all_users:
        print(user)