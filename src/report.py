def print_report(current_connections, max_connections, connection_usage, database_size):
    print(f"    Active connections: {current_connections} / {max_connections}")
    print(f"    Connection usage: {connection_usage:.0f}%")
    print(f"    Database size: {database_size}")
    print()

def print_active_queries(queries):
    print("============================")
    print(" Active queries:")
    print("============================")
    if not queries:
        print("     No active queries")
        return
    
    for pid, user, sql, query_start, duration in queries:

        if len(sql) > 100:
            sql = sql[:100] + "..."


        print("------------------------------------")
        print(f"    PID:  {pid}")
        print(f"    User: {user}")
        print(f"    Query: {sql}")
        print(f"    Started: {query_start}")
        print(f"    Duration: {duration}")
        print()

def print_long_running_queries(queries):
    print("============================")
    print(" Long-running queries:")
    print("============================")
    if not queries:
        print("     No long-running queries")
        return
    
    for pid, user, sql, query_start, duration in queries:

        if len(sql) > 100:
            sql = sql[:100] + "..."


        print("------------------------------------")
        print(f"    PID:  {pid}")
        print(f"    User: {user}")
        print(f"    Query: {sql}")
        print(f"    Started: {query_start}")
        print(f"    Duration: {duration}")
        print()

def print_table_sizes(table_sizes):
    print("============================")
    print("Table sizes:")
    print("============================")
    if not table_sizes:
        print("     No table sizes")
        return
    
    for schemaname, tablename, size in table_sizes:
        print("------------------------------------")
        print(f"    Schema:  {schemaname}")
        print(f"    Table: {tablename}")
        print(f"    Size: {size}")
        print()

def print_locks(locks):

    print("============================")
    print(" Locks:")
    print("============================")

    if not locks:
        print("     No locks")
        return
    
    for waiting_pid, waiting_user, waiting_query, holding_pid, holding_user, holding_query in locks:
        print("------------------------------------")

        print(f"    Waiting PID: {waiting_pid}")
        print(f"    Waiting User: {waiting_user}")
        print(f"    Waiting Query: {waiting_query}")

        print()

        print(f"    Holding PID: {holding_pid}")
        print(f"    Holding User: {holding_user}")
        print(f"    Holding Query: {holding_query}")

def print_monitor_report(report):
    print("============================")
    print(" PostgreSQL Health Monitor")
    print("============================")
    print()
    print(f"Report time: {report['report_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print_status(report["status_info"])
    
    
    print_report(
        report["current_connections"],
        report["max_connections"],
        report["connection_usage"],
        report["database_size"],
    )

    print_active_queries(
        report["active_queries"]
    )

    print_long_running_queries(
        report["long_running_queries"]
    )

    print_locks(
        report["locks"]
    )

    print_table_sizes(
        report["table_sizes"]
    )

def get_monitor_status(long_queries, connection_usage, warning_threshold, critical_threshold):
    reasons = []
    critical = False

    if long_queries:
        reasons.append("Long-running queries detected")

    if connection_usage >= critical_threshold:
        reasons.append("Connection usage is critically high")
        critical = True
    elif connection_usage >= warning_threshold:
        reasons.append("Connection usage is high")

    if critical:
        return {
            "status": "CRITICAL",
            "reasons": reasons
        }
    elif reasons:
        return {
            "status": "WARNING",
            "reasons": reasons
        }
    else:
        return {
            "status": "OK",
            "reasons": []
    }

def print_status(status_info):
    print(f"Status: {status_info['status']}")

    if status_info["reasons"]:
        print("Reasons:")
        for reason in status_info["reasons"]:
            print(f" - {reason}")

    print()
 