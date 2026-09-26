from datetime import timedelta
import os
from config import LONG_QUERY_THRESHOLD



def load_sql(filename):
    with open(filename) as file:
        content = file.read()
        return content


def execute_one(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone() 
        return result[0]

def execute_all(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall() 
        return result

def get_active_connections(connection):
    return execute_one(
        connection,
        "SELECT count(*) FROM pg_stat_activity;"
    )

def get_database_size(connection):
    return execute_one(
        connection,
        """
        SELECT pg_size_pretty(
            pg_database_size(current_database())
        );
        """
    )




def find_long_running_queries(queries):
    long_running = []

    for pid, user, sql, query_start, duration in queries:
        if duration > LONG_QUERY_THRESHOLD:
            long_running.append((pid, user, sql, query_start, duration))

    return long_running

def get_active_queries(connection):
    query = load_sql("sql/activity.sql")
    return execute_all(
            connection,
            query
        )

def get_table_sizes(connection):
    query = load_sql("sql/table_size.sql")
    return execute_all(
            connection,
            query
        )

def get_locks(connection):
    query = load_sql("sql/locks.sql")
    return execute_all(
            connection,
            query
        )