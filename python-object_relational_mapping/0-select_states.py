#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306,
                        user=username, passwd=password,
                        db=db_name, charset="utf8")

    # Création d'un curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Exécution de la requête SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Récupération et affichage des résultats
    for state in cursor.fetchall():
        print(state)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
    