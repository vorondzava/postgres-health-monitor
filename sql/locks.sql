SELECT
    waiting.pid AS waiting_pid,
    waiting_activity.usename AS waiting_user,
    waiting_activity.query AS waiting_query,
    holding.pid AS holding_pid,
    holding_activity.usename AS holding_user,
    holding_activity.query AS holding_query
FROM pg_locks AS waiting
JOIN pg_locks AS holding
    ON waiting.relation = holding.relation
JOIN pg_stat_activity AS waiting_activity
    ON waiting.pid = waiting_activity.pid
JOIN pg_stat_activity AS holding_activity
    ON holding.pid = holding_activity.pid
WHERE waiting.granted = false
  AND holding.granted = true;