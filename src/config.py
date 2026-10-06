from datetime import timedelta
import os

def get_long_query_threshold():
    try:
        minutes = int(os.getenv("LONG_QUERY_MINUTES", "5"))
        if minutes <= 0:
            print("LONG_QUERY_MINUTES must be greater than 0, using default 5")
            minutes = 5
    except ValueError:
        print("Invalid LONG_QUERY_MINUTES value, using default 5")
        minutes = 5

    return  timedelta(minutes=minutes)

def get_int_setting(name, default, min_value, max_value):
    try:
        value = int(os.getenv(name, default))
        if not min_value <= value <= max_value:
            print(f"{name} must be between X and Y, using default")
            value = default
    except ValueError:
        print(f"Invalid {name} value, using default")
        value = default

    return  value

def get_connection_usage_critical():
    return get_int_setting("CONNECTION_USAGE_CRITICAL",90,1,100)

def get_connection_usage_warning():
    return get_int_setting("CONNECTION_USAGE_WARNING",80,1,100)