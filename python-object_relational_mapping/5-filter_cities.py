#!/usr/bin/python3
"""
This module lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données avec charset="utf8"
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_user, passwd=mysql_password,
                         db=database_name, charset="utf8")

    cursor = db.cursor()

    # Requête SQL
    query = """
    SELECT cities.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    # Affichage des villes
    if cities:
        print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
