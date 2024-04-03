-- Jeux de données OK (ça doit marcher)
INSERT INTO Client VALUES (10000001, 'Amy', '07 00 32 46 75');
INSERT INTO Client VALUES (10000002, 'Bob', '07 87 62 34 90');
INSERT INTO Client VALUES (10000003, 'Cathy', '07 00 32 46 75');
INSERT INTO Client VALUES (10000004, 'David', '07 87 62 34 90');
INSERT INTO Client VALUES (10000005, 'Eva', '07 00 32 46 75');


INSERT INTO Marque VALUES (1, 'Canon', 'le premier choix d''innombrables amateurs et professionnels de la photographie.');
INSERT INTO Marque VALUES (2, 'Nikon', 'Un compagnon fidèle pour les photographes de paysages et de faune.');
INSERT INTO Marque VALUES (3, 'Sony', 'Un choix populaire pour les photographes de rue et de portrait.');
INSERT INTO Marque VALUES (4, 'Panasonic', 'Un choix populaire pour les vidéastes et les photographes de voyage.');
INSERT INTO Marque VALUES (5, 'Leica','il symbolise le luxe et la pureté des arts photographiques.');


-- Date en format par défaut SQLite : 'YYYY-MM-DD'
INSERT INTO Camera VALUES (1024, 1, 'EOS R6 Mark II', '2020-12-03', 'parfait', '2000');
INSERT INTO Camera VALUES (1025, 2, 'D850', '2019-08-24', 'correct', '1500');
INSERT INTO Camera VALUES (1026, 3, 'Alpha 7 III', '2021-02-08', 'tresbon', '1800');
INSERT INTO Camera VALUES (1027, 1, 'EOS 5D Mark IV', '2018-09-08', 'correct', '2500');
INSERT INTO Camera VALUES (1028, 4, 'Lumix GH5', '2019-03-15', 'parfait', '1700');


INSERT INTO Dossier VALUES (9001010, 10000001, 1024, '2024-02-19');
INSERT INTO Dossier VALUES (9001011, 10000002, 1025, '2024-03-27');
INSERT INTO Dossier VALUES (9001012, 10000003, 1026, '2023-04-15');
INSERT INTO Dossier VALUES (9001013, 10000003, 1027, '2023-05-23');


INSERT INTO Wishlist VALUES (10000001, 1024);
INSERT INTO Wishlist VALUES (10000002, 1024);
INSERT INTO Wishlist VALUES (10000003, 1026);
INSERT INTO Wishlist VALUES (10000004, 1028);