USE ansi_sql_db;
SELECT e.title, COUNT(s.session_id) AS session_count
FROM events e
JOIN sessions s ON e.event_id = s.event_id
GROUP BY e.event_id
ORDER BY session_count DESC
LIMIT 1;
