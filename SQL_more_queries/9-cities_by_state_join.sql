-- script that lists all cities contained in the database
FROM cities
SELECT cities.id, cities.name, states.name
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
