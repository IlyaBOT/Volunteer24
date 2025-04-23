import pandas as pd

# Указываем путь к CSV файлу
csv_file = "C:\Users\User\Downloads\Telegram Desktop\тестовые данные.csv"

# Читаем CSV файл в DataFrame (структура данных Pandas)
df = pd.read_csv(csv_file)

# Теперь df — это DataFrame с данными из CSV
print(df.head())  # Показывает первые 5 строк
