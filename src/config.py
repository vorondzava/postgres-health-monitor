from datetime import timedelta
import os

try:
    long_query_minutes = int(os.getenv("LONG_QUERY_MINUTES", "5"))
except ValueError:
    print("Invalid LONG_QUERY_MINUTES value, using default 5")
    long_query_minutes = 5

LONG_QUERY_THRESHOLD = timedelta(minutes=long_query_minutes)