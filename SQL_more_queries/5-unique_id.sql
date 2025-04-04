-- script that creates the table unique_id
create table if not EXISTS unique_id(
    id INT not null default 1 unique,
    name VARCHAR(256)
);
