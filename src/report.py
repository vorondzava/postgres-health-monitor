def print_report(active_connections, database_size):
    print("============================")
    print(" PostgreSQL Health Monitor")
    print("============================")

    print()

    print(f"Active connections: {active_connections}")
    print(f"Database size: {database_size}")