-- Jeux de données NOK (ne doit pas marcher àprès avoir éxécuté le jeux de données NOK)

-- Erreur : Client avec numéro existant
INSERT INTO Client VALUES (10000001, 'April', '06 10 12 23 34');
-- Erreur : Client avec numéro type incorrect
INSERT INTO Client VALUES ('00000006', 'April', '06 10 12 23 34'); --type TEXT au lieu de INTEGER

-- Erreur : Marque existante
INSERT INTO Marque VALUES ('10', 'Canon', 'le premier choix d`innombrables amateurs et professionnels de la photographie.');
-- Erreur : Marque sans nom
INSERT INTO Marque VALUES (6, NULL, 'le premier choix d`innombrables amateurs et professionnels de la photographie.');

-- Erreur : prix négatif
INSERT INTO Camera VALUES (1031, 1, 'EOS R7', '1111-01-01', 'correct', -2500.00);
-- Erreur : qualité incorrecte(qualité doit être 'parfait', 'correct' ou 'tresbon')
INSERT INTO Camera VALUES (1032, 1, 'EOS R7', '2023-01-01', 'moyen', 2500.00);
-- Erreur : Camera avec numéro existant
INSERT INTO Camera VALUES (1024, 3, 'Alpha 7 II', '2020-03-14"', 'tresbon', 1700);
-- Erreur : Camera sans marque
INSERT INTO Camera VALUES (1033, NULL, 'EOS R7', '2023-01-01', 'correct', 2500.00);
-- Erreur : Camera de marque inconnue
INSERT INTO Camera VALUES (1034, 10, 'EOS R7', '2023-01-01', 'correct', 2500.00);
-- Erreur : Camera avec numéro existant
INSERT INTO Camera VALUES (1024, 3, 'Alpha 7 II', '2020-03-14"', 'tresbon', 1700);

-- Erreur : Dossier avec numéro existant
INSERT INTO Dossier VALUES (9001010, 11111111, 1024, '2024-02-19');
-- Erreur : Client inexistant
INSERT INTO Dossier VALUES (9001014, 10000006, 1024, '2024-02-19');
-- Erreur : Dossier sans client
INSERT INTO Dossier VALUES (9001015, NULL, 1024, '2024-02-19');

-- Erreur : Dossier sans camera
INSERT INTO Dossier VALUES (9001016, 10000001, NULL, '2024-02-19');
-- Erreur : Camera inexistante
INSERT INTO Dossier VALUES (9001017, 10000001, 11111111, '2024-02-19');