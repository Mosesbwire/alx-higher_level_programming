-- group values under an alias

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
