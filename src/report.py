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
        print(f"PID:  {pid}")
        print(f"User: {user}")
        print(f"Query: {sql}")
        print(f"Started: {query_start}")
        print()

def print_table_sizes(table_sizes):
    print("============================")
    print("Table sizes:")
    print("============================")
    if not table_sizes:
        print("No table sizes")
        return
    
    for schemaname, tablename, size in table_sizes:
        print("----------------------------")
        print(f"Schema:  {schemaname}")
        print(f"Table: {tablename}")
        print(f"Size: {size}")
        print()

def print_locks(locks):
    print("============================")
    print("Locks:")
    print("============================")

    if not locks:
        print("No locks")
        return
    
    for waiting_pid, waiting_user, waiting_query, holding_pid, holding_user, holding_query in locks:
        print("----------------------------")

        print(f"Waiting PID: {waiting_pid}")
        print(f"Waiting User: {waiting_user}")
        print(f"Waiting Query: {waiting_query}")

        print()

        print(f"Holding PID: {holding_pid}")
        print(f"Holding User: {holding_user}")
        print(f"Holding Query: {holding_query}")