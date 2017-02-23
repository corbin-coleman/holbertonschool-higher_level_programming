-- Find the three hottest states
-- Limit output to 3
SELECT state, MAX(value) max_temp FROM temperatures GROUP BY state ORDER BY state LIMIT 3;
