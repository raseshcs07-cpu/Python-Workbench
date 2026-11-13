-- celebs table
CREATE TABLE celebs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO celebs (name, age)
VALUES
    ('Tom Holland', 29),
    ('Zendaya', 29),
    ('Robert Downey Jr', 61);

SELECT * FROM celebs;



-- table_name table
CREATE TABLE table_name (
   column_1 data_type, 
   column_2 data_type, 
   column_3 data_type
);

SELECT * FROM table_name;



-- newceleb table
CREATE TABLE newceleb (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO newceleb (
    id, name, birth_year)
VALUES (1, 'Justin Bieber', 1994); 

INSERT INTO newceleb (
    id, name, birth_year) 
VALUES (2, 'Beyonce Knowles', 1981); 

INSERT INTO newceleb (
    id, name, birth_year) 
VALUES (3, 'Jeremy Lin', 1988); 

INSERT INTO newceleb (
    id, name, birth_year) 
VALUES (4, 'Taylor Swift', 1989); 

ALTER TABLE newceleb
RENAME COLUMN age TO birth_year;

PRAGMA table_info(newceleb);

ALTER TABLE newceleb 
ADD COLUMN instagram_handle TEXT;

UPDATE newceleb 
SET instagram_handle = '@taylorswift' 
WHERE id = 4; 

DELETE FROM newceleb
WHERE instagram_handle IS NULL;

SELECT * FROM newceleb;

SELECT name FROM newceleb;


-- awards table
CREATE TABLE awards (
   id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
   recipient TEXT NOT NULL,
   award_name TEXT DEFAULT 'Grammy'
);

INSERT INTO awards(
    id, award_name)  
    VALUES (1, 'VMA'); 

INSERT INTO awards(
    id, recipient, award_name)  
    VALUES (1, 'Kendrick Lamar', 'VMA'); 

SELECT * FROM awards;




/*
CREATE TABLE
Preview: Docs Creates a new table within a database.
 creates a new table.

INSERT INTO
Preview: Docs Adds new rows of data into a database table.
 adds a new row to a table.

SELECT
Preview: Docs Every SQL query will begin with the SELECT command to fetch data from one or more tables.
 queries data from a table.

ALTER TABLE
Preview: Docs Loading link description
 changes an existing table.

UPDATE
Preview: Docs Edits row(s) in a table.
 edits a row in a table.

DELETE FROM
Preview: Docs Removes existing row(s) from a table. If a WHERE statement is excluded, all rows in the table will be deleted.
 deletes rows from a table.
*/