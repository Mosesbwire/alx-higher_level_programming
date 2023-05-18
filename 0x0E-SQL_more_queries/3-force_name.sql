-- create a table and enforce NOT NULL constraint on name column

CREATE TABLE IF NOT EXISTS force_name(
    id INTEGER,
    name VARCHAR(256) NOT NULL);
