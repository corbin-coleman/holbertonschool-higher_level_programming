-- Find all records from second_table with a score >= 10
-- Sort the output with the highest scores at top
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
