import db

# ---------------Requête sélection/projection---------------
# Afficher toutes les caméras
def select_all_cameras(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Camera")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# ---------------Requête opérateurs ensemblistes---------------
# Les clients qui ont acheté un appareil photo et qui ont l'appareil photo sur leur liste de souhaits.
def select_clients_ayant_achete_une_camera(conn):

    cur = conn.cursor()
    cur.execute("SELECT numCli FROM Dossier INTERSECT SELECT numCli FROM Wishlist")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# ---------------Requête jointure/aggrégation---------------
# Afficher les caméras avec leur marque
def select_cameras_marque(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM Camera JOIN Marque ON Camera.numM = Marque.numM")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# ---------------Requête jointure/aggrégation---------------
# Afficher le nombre de caméras par marque
def select_nombre_cameras_marque(conn):

    cur = conn.cursor()
    cur.execute("SELECT nomM, COUNT(*) FROM Camera JOIN Marque ON Camera.numM = Marque.numM GROUP BY nomM")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# ---------------Requête paramétées---------------
# Afficher les caméras d'une marque donnée
def select_cameras_marque_param(conn, marque):

    cur = conn.cursor()
    cur.execute("SELECT * FROM Camera JOIN Marque ON Camera.numM = Marque.numM WHERE nomM = ?", (marque,))

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("Aucune caméra de la marque\n", marque)

# Indique combien de personnes ont ajouté cette caméra à leur Wishlist
def select_nb_personnes_wishlist(conn, camera):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Wishlist WHERE numCam = ?", (camera,))

    rows = cur.fetchone()

    print("Il y a", rows[0], "personnes qui ont ajouté cette caméra à leur Wishlist\n")

# Vérifiez si la camera a été vendu
def select_camera_vendu(conn, camera):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Dossier WHERE numCam = ?", (camera,))

    rows = cur.fetchone()

    if rows[0] > 0:
        print("Cette caméra a été vendu\n")
    else:
        print("Cette caméra n'a pas été vendu\n")

# Afficher les caméras dont le prix est inférieur à prix saisie par l'utilisateur
def select_cameras_prix_inf(conn, prix):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Camera WHERE prix < ?", (prix,))

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("Aucune caméra dont le prix est inférieur à", prix)


def select_param():
    database = "data/camera.db"
    conn = db.creer_connexion(database)

    while True:
        print('''-----------------------------------------------------------------------
                Veuillez sélectionner le sujet de votre demande:
                a. Afficher les caméras d'une marque donnée
                b. Indiquer combien de personnes ont ajouté cette caméra à leur Wishlist
                c. Vérifiez si la camera a été vendu
                d. Afficher les caméras dont le prix est inférieur à prix saisie par l'utilisateur
                q. Quiiter\n''')

        choix = input("Votre choix: ")
        if choix == 'a':
            marque = input("Entrez la marque de la caméra: ")
            select_cameras_marque_param(conn, marque)

        elif choix == 'b':
            camera = input("Entrez le numéro de la caméra: ")
            select_nb_personnes_wishlist(conn, camera)

        elif choix == 'c':
            camera = input("Entrez le numéro de la caméra: ")
            select_camera_vendu(conn, camera)

        elif choix == 'd':
            prix = input("Entrez le prix: \n")
            try:
                prix = float(prix)
                select_cameras_prix_inf(conn, prix)
            except ValueError:
                print("Veuillez entrer un nombre: ")

        elif choix == 'q':
            print("Au revoir!")
            break

        else:
            print("Veuillez entrer un choix valide")
            select_param()

    conn.close()

# demande à l'utilisateur de saisir le SQL REQUETE à exécuter
def select_sql():
    database = "data/camera.db"
    conn = db.creer_connexion(database)

    while True:
        sql = input("Entrez votre requête SQL: ")
        try:
            cur = conn.cursor()
            cur.execute(sql)

            rows = cur.fetchall()

            for row in rows:
                print(row)

        except Exception as e:
            print(e)

        choix = input("Voulez-vous continuez? (o/n): ")
        if choix == 'n':
            print("Au revoir!")
            break
        elif choix == 'o':
            continue
        else:
            print("Veuillez entrer un choix valide")
            break

def main():
    # Nom de la BD à créer
    db_file = "data/camera.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    if conn is not None:
        # Remplir la BD
        print("1. On crée la bd et on l'initialise avec des premières valeurs.")
        db.mise_a_jour_bd(conn, "data/main.sql")
        db.mise_a_jour_bd(conn, "data/Jeu_de_Test_OK.sql")

        # Lire la BD
        print("2. Liste de toutes les caméras")
        select_all_cameras(conn)
    else:
        print("Erreur! Impossible de créer la base de données.")

if __name__ == "__main__":
    main()