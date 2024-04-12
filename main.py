import db

# Requête sélection/projection
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

# Requête opérateurs ensemblistes
# donner les clients qui ont déjà acheté une caméra
def select_clients_ayant_achete_une_camera(conn):

    cur = conn.cursor()
    cur.execute("SELECT numCli, nomCli FROM Client INTERSECT SELECT numCli FROM Dossier")

    rows = cur.fetchall()

    for row in rows:
        print(row)

# Requête jointure/aggrégation
# Afficher les caméras avec leur marque
def select_cameras_marque(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM Camera JOIN Marque ON Camera.numM = Marque.numM")

    rows = cur.fetchall()

    for row in rows:
        print(row)

# Requête jointure/aggrégation
# Afficher le nombre de caméras par marque
def select_nombre_cameras_marque(conn):

    cur = conn.cursor()
    cur.execute("SELECT nomM, COUNT(*) FROM Camera JOIN Marque ON Camera.numM = Marque.numM GROUP BY nomM")

    rows = cur.fetchall()

    for row in rows:
        print(row)

# Requête paramétées
# Afficher les caméras d'une marque donnée
def select_cameras_marque_param(conn, marque):

    cur = conn.cursor()
    cur.execute("SELECT * FROM Camera JOIN Marque ON Camera.numM = Marque.numM WHERE nomM = ?", (marque,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_param():
    database = "data/camera.db"
    conn = db.creer_connexion(database)
    marque = input("Entrez la marque de la caméra: ")
    select_cameras_marque_param(conn, marque)
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