-- a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table(id INT, name VARCHAR(256), score INT);
INSERT second_table VALUES (1,'John', 10);
INSERT second_table VALUES (2, 'Alex', 3);
INSERT second_table VALUES (3, 'Bob', 14);
INSERT second_table VALUES (4, 'George', 8);
