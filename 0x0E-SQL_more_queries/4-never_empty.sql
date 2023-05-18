-- create a table with the id column having a default value

CREATE TABLE IF NOT EXISTS id_not_null(
    id INTEGER DEFAULT 1,
    name VARCHAR(256));
