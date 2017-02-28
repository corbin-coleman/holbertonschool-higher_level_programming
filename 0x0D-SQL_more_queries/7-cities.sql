-- Create a database and a table
-- table must be created in the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT PRIMARY KEY AUTO_INCREMENT, state_id INT, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id), name VARCHAR(256) NOT NULL);
