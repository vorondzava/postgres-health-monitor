
WITH 
database_size AS (SELECT datname as database,
pg_size_pretty(pg_database_size(datname)) as size
FROM pg_database),
active_connections AS (SELECT count(*) AS active_queries
FROM pg_stat_activity
WHERE state = 'active'),
table_size AS (select 
tablename, pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)) as size
FROM pg_tables)


