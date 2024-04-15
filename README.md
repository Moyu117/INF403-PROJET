# INF403-PROJET Second-hand camera trading platform database
### Author: ZHANG Yuchen, ZHANG Mengtong
  
#### Introduction: Implement a second-hand camera trading platform database from 0 through UML modeling and SQL statements  

---
## Utilisation:

Il est possible d'utiliser le code de ce projet de deux façons.

### Utilisation non-interactive

Dans un terminal:

    # Pour Linux
    python3 main.py

    # Pour Windows
    py main.py

Cela va exécuter la méthode main contenue dans le script `main.py`.

Après avoir exécuté cette étape, le fichier **camera.db** sera créé dans le dossier ***data***, initialisé avec le contenu de `data/Jeu_de_Test_OK`.

### Utilisation interactive

Dans un terminal, on peut exécuter `python3` (`py` sous Windows), puis entrer
le code nécessaire à l'exécution des différentes requêtes. C'est pratique pour
faire des tests rapides:

    $ python3
    Python 3.10.13 (main, Apr  3 2024, 17:08:15) [GCC 9.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import main
    >>> import db
    >>> f = "data/camera.db"
    >>> conn = db.creer_connexion(f)
    >>> main.select_all_cameras(conn)
    (1024, 1, 'EOS R6 Mark II', '2020-12-03', 'parfait', 2000.0)
    (1025, 2, 'D850', '2019-08-24', 'correct', 1500.5)
    (1026, 3, 'Alpha 7 III', '2021-02-08', 'tresbon', 1800.0)
    (1027, 1, 'EOS 5D Mark IV', '2018-09-08', 'correct', 2500.0)
    (1028, 4, 'Lumix GH5', '2019-03-15', 'parfait', 1700.0)
    (1029, 5, 'M10', '2020-12-03', 'parfait', 2000.0)
    (1030, 1, 'EOS 4000D', '2023-09-08', 'correct', 2500.0)

    >>> main.select_clients_ayant_achete_une_camera(conn)
    (10000001,)
    (10000002,)
    (10000003,)

    >>> main.select_cameras_marque(conn)
    (1024, 1, 'EOS R6 Mark II', '2020-12-03', 'parfait', 2000.0, 1, 'Canon', "le premier choix  d'innombrables amateurs et professionnels de la photographie.")
    (1025, 2, 'D850', '2019-08-24', 'correct', 1500.5, 2, 'Nikon', 'Un compagnon fidèle pour les    photographes de paysages et de faune.')
    (1026, 3, 'Alpha 7 III', '2021-02-08', 'tresbon', 1800.0, 3, 'Sony', 'Un choix populaire pour   les photographes de rue et de portrait.')
    (1027, 1, 'EOS 5D Mark IV', '2018-09-08', 'correct', 2500.0, 1, 'Canon', "le premier choix  d'innombrables amateurs et professionnels de la photographie.")
    (1028, 4, 'Lumix GH5', '2019-03-15', 'parfait', 1700.0, 4, 'Panasonic', 'Un choix populaire     pour les vidéastes et les photographes de voyage.')
    (1029, 5, 'M10', '2020-12-03', 'parfait', 2000.0, 5, 'Leica', 'il symbolise le luxe et la   pureté des arts photographiques.')
    (1030, 1, 'EOS 4000D', '2023-09-08', 'correct', 2500.0, 1, 'Canon', "le premier choix   d'innombrables amateurs et professionnels de la photographie.")

    >>> main.select_nombre_cameras_marque(conn)
    ('Canon', 3)
    ('Leica', 1)
    ('Nikon', 1)
    ('Panasonic', 1)
    ('Sony', 1)


Requête paramétées: 