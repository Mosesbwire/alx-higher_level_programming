-- Gets the max temp value of each state grouping the data by state

SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
