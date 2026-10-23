from datetime import datetime

import psycopg
from config import (
    get_connection_usage_critical, 
    get_connection_usage_thresholds, 
    get_connection_usage_warning
)
from database import (
    check_connection, 
    get_connection
)
from monitor import (
    get_active_connections,
    get_database_size,
    get_active_queries,
    get_locks,
    get_table_sizes,
    find_long_running_queries,
    get_test
)
from report import (
    get_monitor_status,
    print_monitor_report
)
import time
import logging


logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)



def run_monitor(): 
    start_time = time.time()
    report_time = datetime.now()
    connection = None
    try:
        connection = get_connection() #Получаем подключение
        

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

        warning_threshold, critical_threshold = get_connection_usage_thresholds(warning_threshold, critical_threshold)
        
        status = get_monitor_status(queries_long, connection_usage, warning_threshold, critical_threshold)
        reasons_text = ", ".join(status["reasons"])
        if status["status"] == "WARNING":
            logging.warning(f"WARNING - Monitor status: WARNING - {reasons_text}")
        elif status["status"] == "CRITICAL":
            logging.error(f"ERROR - Monitor status: CRITICAL - {reasons_text}")

        #

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

        
        logging.info("Monitor completed successfully")

    except ValueError as error:
        print(f"Configuration error: {error}")
        raise

    except psycopg.OperationalError as error:
        logging.error(f"Database connection error: {error}")

    except psycopg.Error as error:
        logging.exception(f"Database query error: {error}")
        return 
        
    finally: #Поэтому его часто используют для вещей, которые обязательно нужно выполнить
        if connection is not None:
            connection.close()

        end_time = time.time()
        logging.info(f"Execution time: {end_time - start_time:.2f} seconds")
    


run_monitor()
