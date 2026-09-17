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

def get_locks(connection):

    return execute_all(
        connection,
        """
        SELECT
    waiting.pid AS waiting_pid,
    waiting_activity.usename AS waiting_user,
    waiting_activity.query AS waiting_query,
    holding.pid AS holding_pid,
    holding_activity.usename AS holding_user,
    holding_activity.query AS holding_query
FROM pg_locks AS waiting
JOIN pg_locks AS holding
    ON waiting.relation = holding.relation
JOIN pg_stat_activity AS waiting_activity
    ON waiting.pid = waiting_activity.pid
JOIN pg_stat_activity AS holding_activity
    ON holding.pid = holding_activity.pid
WHERE waiting.granted = false
  AND holding.granted = true AND waiting.pid <> holding.pid;
        """
    )