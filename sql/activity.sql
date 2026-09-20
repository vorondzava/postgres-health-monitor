SELECT
    usename,
    datname,
    query,
    query_start
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY query_start DESC;