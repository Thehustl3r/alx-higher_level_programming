-- sql command
-- sql cmd
CREATE TABLE IF NOT EXISTS unique_id(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256),
	UNIQUE KEY unique_id_idx(id)
);
