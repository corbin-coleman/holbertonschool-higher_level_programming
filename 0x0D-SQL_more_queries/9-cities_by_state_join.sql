-- List information from two tables
-- use the JOIN operation
SELECT DISTINCT cities.id, cities.name, states.name FROM states JOIN cities WHERE cities.state_id = states.id ORDER BY cities.id ASC;
