from database import get_connection
from monitor import (
    get_active_connections,
    get_database_size,
    get_active_queries
)
from report import print_report


connection = get_connection() #Получаем подключение

active = get_active_connections(connection) #Передаём его в мониторинг
size = get_database_size(connection)

print_report(active,size)

queries = get_active_queries(connection)
print()
print("Active queries:")
print(queries)
