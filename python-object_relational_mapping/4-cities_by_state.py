#!/usr/bin/python3
"""This module lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_user, passwd=mysql_password,
                         db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a query to fetch all cities from the database
    query = "SELECT cities.id, cities.name," \
    "states.name FROM cities INNER JOIN states" \
    "ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)

    # Fetch all results
    cities = cursor.fetchall()

    # Display results as specified
    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
