from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Замените на ваши параметры подключения к MySQL
DATABASE_URL = "mysql+pymysql://username:password@localhost/db_name"  # для PyMySQL
# DATABASE_URL = "mysql+mysqlclient://username:password@localhost/db_name"  # для mysqlclient

# Создаем движок для подключения
engine = create_engine(DATABASE_URL, pool_recycle=3600)

# Сессия
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем базовый класс для моделей
Base = declarative_base()

# Функция для получения сессии с БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()