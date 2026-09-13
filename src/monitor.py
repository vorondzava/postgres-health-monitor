def execute_query(connection, query):
    cursor = connection.cursor() #создаём объект, который будет выполнять SQL-команды через соединение.

    cursor.execute(query)#передаем запрос

    result = cursor.fetchone() #получаем один столбец результата

    return result[0]

def get_active_connections(connection):
    return execute_query(
        connection,
        "SELECT count(*) FROM pg_stat_activity;"
    )

def get_database_size(connection):
    return execute_query(
        connection,
        """
        SELECT pg_size_pretty(
            pg_database_size(current_database())
        );
        """
    )