CREATE TABLE friends (
	id INTEGER,
	name TEXT,
	birthday DATE
);

/*add Jane Doe to friends + 2 other people*/
INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Jane Doe', '1990-05-30');

INSERT INTO friends (id, name, birthday) 
VALUES (2, 'BFF One', 'YYYY-MM-DD');

INSERT INTO friends (id, name, birthday) 
VALUES (3, 'BFF Two', 'YYYY-MM-DD');

/*Check if it's been added*/
SELECT * 
FROM friends;

/*add a new column email*/
ALTER TABLE friends 
ADD COLUMN email TEXT; 

/*update Jane's email*/
UPDATE friends
SET email = 'jane@codecademy.com'
WHERE id = 1;

/*delete jane*/
DELETE FROM friends
WHERE id = 1;

/*result of table*/
SELECT * 
FROM friends;