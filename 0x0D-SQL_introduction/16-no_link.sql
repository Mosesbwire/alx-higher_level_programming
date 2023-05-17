-- lists all records of a given table

SELECT score, name FROM second_table WHERE name IS NULL OR name IS NOT NULL ORDER BY score DESC;
