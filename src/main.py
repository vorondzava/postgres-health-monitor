from database import get_connection
from monitor import get_active_connections, get_database_size


connection = get_connection() #Получаем подключение

active = get_active_connections(connection) #Передаём его в мониторинг
print("Active connections:")
print(active)

size = get_database_size(connection)
print("Database size:")
print(size)