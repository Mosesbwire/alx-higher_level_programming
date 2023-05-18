-- create a database with a table. Id column with auto generated value unique and primary key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INTEGER AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
    name VARCHAR(256) NOT NULL);
