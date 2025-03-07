#!/usr/bin/python3
"""Module to list all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_user, passwd=mysql_password,
                         db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))  # Use a tuple to pass the parameter safely

    # Fetch all results
    states = cursor.fetchall()

    # Check if any states were found, and display them
    if states:
        for state in states:
            print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
