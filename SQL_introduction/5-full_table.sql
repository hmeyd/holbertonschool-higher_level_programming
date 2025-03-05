-- script that prints the following description of a table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
