--  Read user
-- The GRANT ALL PRIVILEGES statement then grants all privileges on all databases and tables in the server to the user
-- The WITH GRANT OPTION clause allows the user to grant privileges to other users.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
