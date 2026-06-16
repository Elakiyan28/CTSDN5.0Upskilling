USE ansi_sql_db;
SELECT u.full_name AS organizer, COUNT(e.event_id) AS total_events, e.status
FROM users u
JOIN events e ON u.user_id = e.organizer_id
GROUP BY u.user_id, e.status;
