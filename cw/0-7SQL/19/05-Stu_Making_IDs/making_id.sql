SELECT * FROM people;

INSERT INTO people(full_name, has_pet, pet_type,pet_name, pet_age)
VALUES 
('Name1',false, 'lion','pet5',10)

DELETE from people WHERE full_name = 'Name1' and pet_type='lion'
DROP TABLE people;

CREATE TABLE public.people
(
	id SERIAL PRIMARY KEY,
    full_name  VARCHAR(30) NOT NULL,
    has_pet boolean DEFAULT false,
    pet_type VARCHAR(30) NOT NULL,
    pet_name VARCHAR(30),
    pet_age integer
)

INSERT INTO people(full_name, has_pet, pet_type,pet_name, pet_age)
VALUES 
('Name1',false, 'lion','pet1',10),
('Name1',false, 'lion','pet2',11),
('Name1',false, 'lion','pet3',12),
('Name1',false, 'lion','pet4',13),
('Name1',false, 'lion','pet5',14)

DELETE from people WHERE id = 1

UPDATE people 
SET full_name = 'Name3', has_pet = true, pet_name = 'Tiger', pet_type = 'Lion'
WHERE id = 3



