-- create a table with id field having a default value and is unique on inserts

CREATE TABLE IF NOT EXISTS unique_id(
    id INTEGER DEFAULT 1 UNIQUE,
    name VARCHAR(256));
