SELECT
    schemaname,
    tablename,
    pg_size_pretty(
        pg_total_relation_size(schemaname || '.' || tablename)
    ) AS size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname || '.' || tablename) DESC;