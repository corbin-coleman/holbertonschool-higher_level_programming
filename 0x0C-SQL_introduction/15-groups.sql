-- Lists number of records with same score in second_table
-- Group and order the records
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
