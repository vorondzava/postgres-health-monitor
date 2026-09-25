from database import get_connection
from monitor import (
    get_active_connections,
    get_database_size,
    get_active_queries,
    get_locks,
    get_table_sizes,
    find_long_running_queries
)
from report import (
    print_locks,
    print_report,
    print_active_queries,
    print_table_sizes,
    print_long_running_queries
)


def run_monitor():
    try:
        connection = get_connection() #Получаем подключение
        if connection is None:
            print("Could not connect to database")
            return

        active = get_active_connections(connection) #Передаём его в мониторинг
        size = get_database_size(connection)
        print_report(active,size)

        queries = get_active_queries(connection)
        print_active_queries(queries)

        queries_long = find_long_running_queries(queries)
        print_long_running_queries(queries_long)

        locks = get_locks(connection)
        print_locks(locks)

        table_sizes = get_table_sizes(connection)
        print_table_sizes(table_sizes)
    finally:
        if connection is not None:
            connection.close()


run_monitor()
