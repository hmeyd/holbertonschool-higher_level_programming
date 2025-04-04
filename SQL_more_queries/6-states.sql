-- Script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utiliser la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Création de la table states
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT, -- id auto-généré, non nul
    name VARCHAR(256) NOT NULL, -- name ne peut pas être NULL
    PRIMARY KEY (id) -- id est la clé primaire
);
