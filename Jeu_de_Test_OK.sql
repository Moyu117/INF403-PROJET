-- Jeux de données OK (ça doit marcher)
INSERT INTO Client VALUES ('10000001', 'Amy', '07 00 32 46 75');
INSERT INTO Client VALUES ('10000002', 'Bob', '07 87 62 34 90');


INSERT INTO Camera VALUES ('1024', 'Canon', 'EOS R6 Mark II', '2020-12-03', 'parfait', '2000');
INSERT INTO Camera VALUES ('1025', 'Nikon', 'D850', '2019-08-24', 'correct', '1500');
INSERT INTO Camera VALUES ('1026', 'Sony', 'Alpha 7 III', '2021-02-08', 'tresbon', '1800');
INSERT INTO Camera VALUES ('1027', 'Canon', 'EOS 5D Mark IV', '2018-09-08', 'correct', '2500');



INSERT INTO Marque VALUES ('01', 'Canon', 'Canon est une marque japonaise spécialisée dans la fabrication d''appareils photo et de matériel photographique.');
INSERT INTO Marque VALUES ('02', 'Nikon', 'Nikon est une marque japonaise spécialisée dans la fabrication d''appareils photo et de matériel photographique.');



INSERT INTO Dossier VALUES ('09001010', '10000001', '1024', '2024-02-19');
INSERT INTO Dossier VALUES ('09001011', '10000002', '1025', '2024-03-27');


INSERT INTO Wishlist VALUES ('10000001', '1026');