-- sql commad
-- sql cmd
-- Create user_0d_1 if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
