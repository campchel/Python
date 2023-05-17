SELECT * from dojos;

INSERT INTO dojos(name)
VALUES ('Judo');
INSERT INTO	dojos(name)
VALUES ('Taekwondo');

DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '5');
DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '6');
DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (`id` = '1');

INSERT INTO dojos('1', 'Coding');

UPDATE `dojos_and_ninjas_schema`.`dojos` SET `name` = 'Coding' WHERE (`id`) = '1';

INSERT INTO dojos(name)
VALUES ('Coding');

DELETE FROM `dojos_and_ninjas_schema`.`dojos` WHERE (dojo_id);

SELECT * from dojos
LEFT JOIN ninjas ON ninjas.dojo_id = dojo.id;
