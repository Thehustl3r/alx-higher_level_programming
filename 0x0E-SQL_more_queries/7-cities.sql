-- sqll commands
-- sql cmd to increments
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256),
	UNIQUE KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
