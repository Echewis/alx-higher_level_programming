-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record where name = California (but the id can be different, as per the example)
SELECT * FROM cities WHERE state_id IN
(SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
