USE ansi_sql_db;
SELECT u.full_name, u.email
FROM users u
WHERE u.user_id NOT IN (
    SELECT r.user_id
    FROM registrations r
    WHERE r.registration_date >= CURDATE() - INTERVAL 90 DAY
);
