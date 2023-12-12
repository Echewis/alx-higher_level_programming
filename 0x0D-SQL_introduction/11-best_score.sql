--  a script that lists all records with a score >= 10 in the table
-- table is filtered for sore equal or greater than 10 and ordered downward
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
