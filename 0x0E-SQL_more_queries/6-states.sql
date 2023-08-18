-- sqll commands
-- sql cmd to increments
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256),
	UNIQUE KEY (id)
);
