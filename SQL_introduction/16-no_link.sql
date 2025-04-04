-- script that lists all records of the table second_table
SELECT score, name
FROM second_table
where name is not NULL
order by score desc
