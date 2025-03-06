--  script that creates a database and a table states
create database if not EXISTS hbtn_0d_usa
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS states (
    id INT IS not null AUTO_INCREMENT,
    name VARCHAR(256) not null
    primary key(id)
);
