-- Requête sélection/projection
-- Afficher toutes les caméras
SELECT * FROM Camera;

-- Requête opérateurs ensemblistes
-- donner les clients qui ont déjà acheté une caméra
SELECT numCli, nomCli FROM Client
INTERSECT
SELECT numCli FROM Dossier;

--Requête jointure/aggrégation
-- Afficher les caméras avec leur marque
SELECT * FROM Camera JOIN Marque ON Camera.numM = Marque.numM;

-- Requête paramétées
-- Afficher les caméras dont le prix est supérieur à 2000
SELECT * FROM Camera WHERE prix > 2000;