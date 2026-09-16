def print_report(active_connections, database_size):
    print("============================")
    print(" PostgreSQL Health Monitor")
    print("============================")
    print()
    print(f"Active connections: {active_connections}")
    print(f"Database size: {database_size}")
    print()

def print_active_queries(queries):
    print("============================")
    print("Active queries:")
    print("============================")
    if not queries:
        print("No active queries")
        return
    
    for pid, user, sql, query_start in queries:

        if len(sql) > 100:
            sql = sql[:100] + "..."


        print("----------------------------")
        print(f"PID: ", {pid})
        print(f"User:", {user})
        print(f"Query:", {sql})
        print(f"Started:", {query_start})
        print()