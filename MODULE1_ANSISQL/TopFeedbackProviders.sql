USE ansi_sql_db;
SELECT u.full_name, COUNT(f.feedback_id) AS feedback_count
FROM users u
JOIN feedback f ON u.user_id = f.user_id
GROUP BY u.user_id
ORDER BY feedback_count DESC
LIMIT 5;
