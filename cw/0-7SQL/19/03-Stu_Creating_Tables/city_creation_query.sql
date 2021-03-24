CREATE TABLE cities(
	city VARCHAR(30) NOT NULL,
	state_name VARCHAR(30) NOT NULL,
	population INT NOT NULL
);

SELECT * FROM cities;

INSERT INTO cities(city, state_name,population)
VALUES
('Alameda','California',79177),
('Mesa','Arizona',496401),
('Boerne','Texas',16056),
('Anaheim','California',352497),
('Tucson','Arizona',535677),
('Garland','Texas',238002)


SELECT city FROM cities;

SELECT city FROM cities
WHERE state_name = 'Arizona';

SELECT city FROM cities
WHERE population <= 100000;

SELECT city FROM cities
WHERE population <= 100000
AND state_name = 'California';



