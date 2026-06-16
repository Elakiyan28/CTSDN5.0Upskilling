USE ansi_sql_db;
SELECT e.title
FROM events e
LEFT JOIN resources r ON e.event_id = r.event_id
WHERE r.resource_id IS NULL;
