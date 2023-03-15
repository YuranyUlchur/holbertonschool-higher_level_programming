-- Cities of California
SELECT * FROM cities
WHERE state = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
