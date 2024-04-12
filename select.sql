-- Requête sélection/projection
-- Afficher toutes les caméras
SELECT * FROM Camera;
-- Afficher toutes les marques
SELECT * FROM Marque;

-- Requête opérateurs ensemblistes
-- donner les clients qui ont déjà acheté une caméra
SELECT numCli, nomCli FROM Client
INTERSECT
SELECT numCli FROM Dossier;

--Requête jointure/aggrégation
-- Afficher les caméras avec leur marque
SELECT * 
FROM Camera JOIN Marque ON Camera.numM = Marque.numM;
-- Afficher le nombre de caméras par marque
SELECT nomM, COUNT(*) 
FROM Camera JOIN Marque ON Camera.numM = Marque.numM 
GROUP BY nomM;

-- Requête paramétées
-- Afficher les caméras dont le prix est inférieur à 2000
SELECT * FROM Camera WHERE prix < 2000;