CREATE TABLE wordassociation(
	author INT,
	word1 VARCHAR,
	word2 VARCHAR ,
	source VARCHAR
	
);

SELECT * FROM wordassociation
WHERE source = 'BC';

SELECT count(*) from wordassociation