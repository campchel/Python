SELECT * from ninjas;

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at)
VALUES ('Annilee', 'Roberts', '21', NOW(), NOW());

INSERT INTO ninjas(first_name, last_name, age)
VALUES ('Ammon', 'Roberts', '19');

INSERT INTO ninjas(first_name, last_name, age)
VALUES ('Emma', 'Roberts', '17');

INSERT INTO ninjas(first_name, last_name, age)
VALUES ('Emilio', 'Giokas', '29');

INSERT INTO ninjas(first_name, last_name, age)
VALUES ('Tyler', 'Sant', '29');

INSERT INTO ninjas(first_name, last_name, age)
VALUES ('Sierra', 'Gower', '27');

INSERT INTO ninjas(first_name, last_name, age)
VALUES ('Ayven', 'Marin', '4');

INSERT INTO ninjas(first_name, last_name, age)
VALUES ('Makai', 'Marin', '1');

INSERT INTO ninjas(first_name, last_name, age)
VALUES ('Dylan', 'Taft', '23');

SELECT * from ninjas
WHERE dojo_id = 2;
SELECT * from ninjas
WHERE dojo_id = 4;
SELECT * from ninjas
WHERE dojo_id = 7;

SELECT id=6
FROM ninjas
JOIN dojos ON ninjas.id = id.ninjas.id;

SELECT *
from ninjas
LEFT JOIN dojos ON ninjas.id =ninjas.id
WHERE id = 6;

SELECT * from ninjas;
INSERT INTO dojos (id)
VALUES ('6');


