import os
import psycopg
from dotenv import load_dotenv

if load_dotenv():   # нашёлся ли файл .env и загрузились ли переменные окружения?
    print(".env loaded")
  
def get_connection():
    # Берём настройки подключения из переменных окружения
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    # Собираем обязательные настройки в один словарь
    config = {
    "DB_HOST": host,
    "DB_NAME": database,
    "DB_USER": user,
    "DB_PASSWORD": password
    }

    missing = [] # Сюда запишем настройки, которых не хватает

    # Проверяем каждую обязательную настройку
    for name, value in config.items():
        if not value:
            missing.append(name)
    # Если чего-то не хватает — подключаться к БД нет смысла
    if missing:
        print(f"Missing configuration: {', '.join(missing)}")
        return None

    try:
        # Создаём подключение к PostgreSQL
        connection = psycopg.connect(
            host=host,
            port=port,
            dbname=database,
            user=user,
            password=password
        )
        
        return connection # Возвращаем готовое подключение вызывающей функции
    
    # Ошибка подключения к PostgreSQL
    except psycopg.OperationalError as error: 
        print(error)
        return None
        # Проблемы с PostgreSQL:
        #   сервер выключен;
        #   неправильный пароль;
        #   нет соединения
