-- a script that creates the table id_not_null on your MySQL server
-- id INT with the default value 1
-- name VARCHAR(256)
-- If the table id_not_null already exists, your script should not fail
CREATE TABLE IF NOT EXISTS id_not_null(id INT NOT NULL, name VARCHAR(256));
