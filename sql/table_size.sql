SELECT
    schemaname,
    tablename,
    pg_size_pretty(
        pg_total_relation_size(schemaname || '.' || tablename)
    ) AS size
FROM pg_tables
WHERE schemaname <> 'pg_catalog' and schemaname <> 'information_schema'
ORDER BY pg_total_relation_size(schemaname || '.' || tablename) DESC;