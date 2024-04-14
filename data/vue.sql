-- Vue de l'historique des achats des clients
-- affiche des informations détaillées sur tous les appareils photo achetés par chaque client, y compris la date d'achat, le modèle d'appareil et le prix.
CREATE VIEW View_ClientPurchases AS
SELECT c.numCli, c.nomCli, ca.modele, ca.qualite, ca.prix, d.dateVente
FROM Client c
JOIN Dossier d ON c.numCli = d.numCli
JOIN Camera ca ON d.numCam = ca.numCam;


-- Vue d'Inventaire des caméras et état des ventes
-- montre l'état de l'inventaire de tous les appareils photo et le nombre de ceux qui ont été vendus, ainsi que la date de la dernière vente pour chaque appareil
CREATE VIEW View_CameraSalesStatus AS
SELECT ca.numCam, ca.modele, COUNT(d.numCam) AS SalesCount, MAX(d.dateVente) AS LastSaleDate
FROM Camera ca
LEFT JOIN Dossier d ON ca.numCam = d.numCam
GROUP BY ca.numCam;
