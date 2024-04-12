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
# donner les clients qui ont déjà acheté une caméra
def select_clients_ayant_achete_une_camera(conn):

    cur = conn.cursor()
    cur.execute("SELECT numCli, nomCli FROM Client INTERSECT SELECT numCli FROM Dossier")

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
        print("Aucune caméra de la marque", marque)

# Indique combien de personnes ont ajouté cette caméra à leur Wishlist
def select_nb_personnes_wishlist(conn, camera):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Wishlist WHERE numCam = ?", (camera,))

    rows = cur.fetchone()

    print("Il y a", rows[0], "personnes qui ont ajouté cette caméra à leur Wishlist")

# Vérifiez si la camera a été vendu
def select_camera_vendu(conn, camera):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Dossier WHERE numCam = ?", (camera,))

    rows = cur.fetchone()

    if rows[0] > 0:
        print("Cette caméra a été vendu")
    else:
        print("Cette caméra n'a pas été vendu")

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
    print('''Veuillez sélectionner le sujet de votre demande:
            a. Afficher les caméras d'une marque donnée
            b. Indiquer combien de personnes ont ajouté cette caméra à leur Wishlist
            c. Vérifiez si la camera a été vendu
            d. Afficher les caméras dont le prix est inférieur à prix saisie par l'utilisateur
            q. Quiiter\n''')

    choix = input("Votre choix: ")
    if choix == 'a':
        marque = input("Entrez la marque de la caméra: ")
        select_cameras_marque_param(conn, marque)
        conn.close()
    elif choix == 'b':
        camera = input("Entrez le numéro de la caméra: ")
        select_nb_personnes_wishlist(conn, camera)
        conn.close()
    elif choix == 'c':
        camera = input("Entrez le numéro de la caméra: ")
        select_camera_vendu(conn, camera)
        conn.close()
    elif choix == 'd':
        prix = input("Entrez le prix: ")
        select_cameras_prix_inf(conn, prix)
        conn.close()
    elif choix == 'q':
        print("Au revoir!")
        conn.close()



def main():
    # Nom de la BD à créer
    db_file = "data/camera.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    # Remplir la BD
    print("1. On crée la bd et on l'initialise avec des premières valeurs.")
    db.mise_a_jour_bd(conn, "data/main.sql")
    db.mise_a_jour_bd(conn, "data/Jeu_de_Test_OK.sql")

    # Lire la BD
    print("2. Liste de toutes les caméras")
    select_all_cameras(conn)
    

if __name__ == "__main__":
    main()