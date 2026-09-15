def execute_one(connection, query):
    cursor = connection.cursor() #создаём объект, который будет выполнять SQL-команды через соединение.
    cursor.execute(query)#передаем запрос
    result = cursor.fetchone() #получаем одну строку результата
    cursor.close()
    return result[0]

def execute_all(connection, query):
    cursor = connection.cursor() #создаём объект, который будет выполнять SQL-команды через соединение.
    cursor.execute(query)#передаем запрос
    result = cursor.fetchall() #получаем все строки результата
    cursor.close()
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

def get_active_queries(connection):
    return execute_all(
            connection,
            """
            SELECT
            pid,
            usename,
            query,
            query_start
            FROM pg_stat_activity
            WHERE state = 'active';
            """
        )