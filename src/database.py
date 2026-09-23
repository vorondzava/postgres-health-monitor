import os
import psycopg
from dotenv import load_dotenv

if load_dotenv():   # нашёлся ли файл .env и загрузились ли переменные окружения?
    print(".env loaded")  
def get_connection():
    try:
        connection = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return connection #момент передачи
    except psycopg.OperationalError as error:
        print(error)
        return None
        
