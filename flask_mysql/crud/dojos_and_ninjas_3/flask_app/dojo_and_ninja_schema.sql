SELECT * FROM dojos;

SELECT * FROM ninjas;

SELECT * FROM dojos WHERE id = 2;

SELECT * FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id=2;

SELECT * FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id=4;

SELECT * FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id=7;


