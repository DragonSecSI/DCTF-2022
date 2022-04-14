USE `database`;

DROP TABLE IF EXISTS `cars`;
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `flags`;

CREATE TABLE IF NOT EXISTS `users` (
    id INTEGER PRIMARY KEY auto_increment,
    name VARCHAR(50),
    surname VARCHAR(50),
    age INTEGER
);

CREATE TABLE IF NOT EXISTS `cars` (
    id INTEGER PRIMARY KEY auto_increment,
    make VARCHAR(50),
    model VARCHAR(50),
    ownerID INTEGER,
    FOREIGN KEY (ownerID) REFERENCES `users`(`id`)
);

CREATE TABLE IF NOT EXISTS `flags` (
	id INTEGER PRIMARY KEY auto_increment,
    flag VARCHAR(50)
);

-- TODO! Only read for branko
GRANT SELECT ON `database`.`cars` TO `branko`;
GRANT SELECT ON `database`.`users` TO `branko`;
GRANT SELECT ON `database`.`flags` TO `branko`;

INSERT INTO `flags` (`flag`) VALUES ('dctf{Pump_1t_up_7h3_s7r3am_353aa965}');


INSERT INTO
    `users`(id, name, surname, age)
VALUES
    (1, "Branko", "Cakarmish", 19),
    (2, "Lara", "Dragar", 28),
    (3, "Lavon", "Tromp", 18),
    (4, "Randal", "Jacobson", 29),
    (5, "Mina", "Lang", 29),
    (6, "Willis", "Little", 34),
    (7, "Haley", "Boyle", 51),
    (8, "Serena", "Kuhic", 21),
    (9, "Chance", "Doyle", 34),
    (10, "Izaiah", "Kuvalis", 19),
    (11, "Ramiro", "Sporer", 21),
    (12, "Cleora", "Turner", 38),
    (13, "Alexa", "Kovacek", 47),
    (14, "Okey", "Kunze", 53),
    (15, "Shane", "Walsh", 46),
    (16, "Vanessa", "Reichel", 31),
    (17, "Enrico", "Bernier", 55),
    (18, "Maybelle", "Hickle", 32),
    (19, "Garry", "Carter", 37),
    (20, "Amanda", "Deckow", 17),
    (21, "Aron", "Greenholt", 34),
    (22, "Garrett", "Dubuque", 41),
    (23, "Mozelle", "Schamberger", 45),
    (24, "Arno", "Mckenzie", 25),
    (25, "Claudie", "Lowe", 17),
    (26, "Janice", "Bogisich", 30),
    (27, "Kenneth", "Dicki", 47);

INSERT INTO
    `cars`(make, model, ownerID)
VALUES
    ("Tesla", "Model S", 2),
    ("Tesla", "Model X", 26),
    ("Tesla", "Model I", 20),
    ("Tesla", "Model B", 10),
    ("Tesla", "Model X", 23),
    ("Tesla", "Model X", 20),
    ("Tesla", "Model 3", 18),
    ("Tesla", "Model H", 9),
    ("Tesla", "Model 3", 10),
    ("Tesla", "Model Z", 20),
    ("Tesla", "Model H", 16),
    ("Tesla", "Model B", 23),
    ("Tesla", "Model X", 6),
    ("Tesla", "Model I", 15),
    ("Tesla", "Model A", 25),
    ("Tesla", "Model K", 4),
    ("Tesla", "Model A", 9),
    ("Tesla", "Model B", 24),
    ("Tesla", "Model A", 9),
    ("Tesla", "Model I", 9),
    ("Tesla", "Model K", 18),
    ("Tesla", "Model S", 2),
    ("Tesla", "Model B", 19),
    ("Tesla", "Model S", 9),
    ("Tesla", "Model X", 5);