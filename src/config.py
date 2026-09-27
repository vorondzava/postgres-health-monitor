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