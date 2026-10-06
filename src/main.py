from datetime import datetime
from config import get_connection_usage_critical, get_connection_usage_warning
from database import check_connection, get_connection
from monitor import (
    get_active_connections,
    get_database_size,
    get_active_queries,
    get_locks,
    get_table_sizes,
    find_long_running_queries
)
from report import (
    get_monitor_status,
    print_monitor_report
)
import time


def run_monitor(): 
    start_time = time.time()
    report_time = datetime.now()
    connection = None
    try:
        connection = get_connection() #Получаем подключение
        if connection is None:
            print("Could not connect to database")
            return

        if not check_connection(connection):
            print("Database connection is not active")
            return

        current_connections, max_connections = get_active_connections(connection) #Получаем текущее и максимальное количество подключений

        connection_usage = (current_connections/max_connections)*100
        
        size = get_database_size(connection)

        queries = get_active_queries(connection)

        queries_long = find_long_running_queries(queries)

        locks = get_locks(connection)

        table_sizes = get_table_sizes(connection)

        warning_threshold = get_connection_usage_warning()

        critical_threshold = get_connection_usage_critical()
        
        status = get_monitor_status(queries_long, connection_usage, warning_threshold, critical_threshold)

        report_data = {
        "current_connections": current_connections,
        "max_connections": max_connections,
        "connection_usage": connection_usage,
        "database_size": size,
        "active_queries": queries,
        "long_running_queries": queries_long,
        "locks": locks,
        "table_sizes": table_sizes,
        "status_info": status,
        "report_time": report_time
        }

        print_monitor_report(report_data)
        
    finally: #Поэтому его часто используют для вещей, которые обязательно нужно выполнить
        if connection is not None:
            connection.close()

        end_time = time.time()
        print(f"Monitor completed in {end_time - start_time:.2f} seconds")
    


run_monitor()
