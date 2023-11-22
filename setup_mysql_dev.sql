-- Script that prepares the MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating new user named : privileges on the db hbnb_dev_db
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting the SELECT privilege to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
