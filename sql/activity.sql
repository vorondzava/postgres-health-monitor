SELECT
    pid,
    usename,
    query,
    query_start,
    clock_timestamp() - query_start as duration
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY query_start DESC;