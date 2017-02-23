-- Find the hottest 3 cities for AUGUST and JULY
-- Find the average for the two months
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
