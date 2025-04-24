import pandas as pd
from sqlalchemy import create_engine, Table, Column, String, MetaData, BigInteger
from sqlalchemy.sql import select

class UserDatabaseManager:
    def __init__(self, db_user='dbuser', db_password='IB2025IB', db_host='localhost', db_port='3306', db_name='db_sport24', csv_file='test_data.csv'):
        self.database_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        self.engine = create_engine(self.database_url)
        self.metadata = MetaData()
        self.users_table = Table('users', self.metadata,
            Column('full_name', String(255), primary_key=True),
            Column('inn', BigInteger),
            Column('phone', BigInteger),
            Column('email', String(255)),
            Column('birth_date', String(20)),
            Column('achievements', String(500))
        )
        self.csv_file = csv_file
        self.metadata.create_all(self.engine)

    def load_csv_to_db(self):
        df = pd.read_csv(self.csv_file)
        df.columns = ['full_name', 'inn', 'phone', 'email', 'birth_date', 'achievements']
        df['inn'] = df['inn'].astype(str).str.replace(r'\D', '', regex=True).astype('int64')
        df['phone'] = df['phone'].astype(str)
        df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)
        df['phone'] = df['phone'].str.replace(r'^8', '7', regex=True)
        df['phone'] = df['phone'].astype('int64')
        df.to_sql('users', con=self.engine, if_exists='replace', index=False)
        print("Данные успешно загружены в базу!")

    def read_all_users(self):
        with self.engine.connect() as connection:
            result = connection.execute(select(self.users_table))
            return result.fetchall()

    def print_all_users(self):
        users = self.read_all_users()
        print("\n📋 Все записи в таблице users:")
        for user in users:
            print(user)

    def read_line(self, line_number):
        df = pd.read_csv(self.csv_file)
        if 0 <= line_number < len(df):
            return df.iloc[line_number]
        return None

    def write_line(self, line_number, name, inn, phone, email, birth, achievements):
        df = pd.read_csv(self.csv_file)
        new_data = {
            'ФИО': name,
            'ИНН': inn,
            'Номер телефона': phone,
            'Электронная почта': email,
            'Дата рождения': birth,
            'Достижения': achievements
        }
        if 0 <= line_number < len(df):
            df.iloc[line_number] = list(new_data.values())
        elif line_number == len(df):
            df.loc[len(df)] = new_data
        df.to_csv(self.csv_file, index=False)
        print(f"Строка {line_number} успешно записана в файл")
