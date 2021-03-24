--CREATE TABLE TABLE_NAME(COLUMN DEFN);
--STEP 1 Create Table
CREATE TABLE people(
	full_name VARCHAR(30) NOT NULL,
	has_pet BOOLEAN DEFAULT FALSE,
	pet_type VARCHAR(10) NOT NULL,
	pet_name VARCHAR(30),
	pet_age INT
);

--STEP 2 Check if you can query
SELECT * FROM people;

--STEP 3 Add some rows
INSERT INTO people(full_name,has_pet,pet_type,pet_name,pet_age)
VALUES
('Name2',true,'cat','Pet2',2),
('Name3',NULL,' ',NULL,NULL),
('Name4',true,'monkey','Pet4',4);

SELECT * FROM people
WHERE pet_age <=4 
AND pet_type = 'cat'


SELECT * FROM people
WHERE pet_age <=4 
AND (
	pet_type = 'cat'
	OR
	pet_type = 'monkey');