-- create database and table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INTEGER AUTO_GENERATE PRIMARY KEY NOT NULL UNIQUE,
    state_id INTEGER NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(state_id),
    name VARCHAR(256) NOT NULL);
