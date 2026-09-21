from database import get_connection
from monitor import (
    get_active_connections,
    get_database_size,
    get_active_queries,
    get_locks,
    get_table_sizes
)
from report import (
    print_locks,
    print_report,
    print_active_queries,
    print_table_sizes
)

connection = get_connection() #Получаем подключение

active = get_active_connections(connection) #Передаём его в мониторинг
size = get_database_size(connection)
print_report(active,size)

queries = get_active_queries(connection)
print_active_queries(queries)

locks = get_locks(connection)
print_locks(locks)

table_sizes = get_table_sizes(connection)
print_table_sizes(table_sizes)
