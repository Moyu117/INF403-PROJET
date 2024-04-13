import sqlite3
import db

#***************************************************
# --------------------- Client ---------------------
#***************************************************
def insert_client(conn):
    try:
        numCli = input("Entrez le numéro du client: ")
        if not numCli.isdigit():
            print("Le numéro du client doit être un entier")
            return
        nom = input("Entrez le nom du client: ")
        phone = input("Entrez le numéro de téléphone du client: ")

        data = (numCli, nom, phone)
        
        cur = conn.cursor()
        cur.execute("INSERT INTO Client VALUES (?, ?, ?)", data)
        conn.commit()
        print("Client ajouté avec succès")
    except sqlite3.IntegrityError as e:
        print(f"Erreur d'ajout du client: {e}")
    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)

def delete_client(conn):
    try:
        numCli = input("Entrez le numéro du client: ")
        if not numCli.isdigit():
            print("Le numéro du client doit être un entier")
            return

        data = (numCli,)
        
        cur = conn.cursor()
        cur.execute("DELETE FROM Client WHERE numCli = ?", data)
        if cur.rowcount == 0:
            print("Aucun client avec ce numéro")
            return
        else:
            conn.commit()
        print("Client supprimé avec succès")

    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)

def update_client(conn):
    try:
        numCli = input("Entrez le numéro du client: ")
        if not numCli.isdigit():
            print("Le numéro du client doit être un entier")
            return
        nom = input("Entrez le nom du client: ")
        phone = input("Entrez le numéro de téléphone du client: ")

        data = (nom, phone, numCli)
        
        cur = conn.cursor()
        cur.execute("UPDATE Client SET nom = ?, phone = ? WHERE numCli = ?", data)
        if cur.rowcount == 0:
            print("Aucun client avec ce numéro")
            return
        else:
            conn.commit()
            print("Client mis à jour avec succès")
    except sqlite3.IntegrityError as e:
        print("Erreur de mise à jour du client: ", e)
    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)


#***************************************************
# --------------------- Camera ---------------------
#***************************************************
def insert_camera(conn):
    pass

def delete_camera(conn):
    pass

def update_camera(conn):
    pass


#***************************************************
# --------------------- Marque ---------------------
#***************************************************
def insert_marque(conn):
    try:
        numM = input("Entrez le numéro de la marque: ")
        if not numM.isdigit():
            print("Le numéro de la marque doit être un entier")
            return
        nomM = input("Entrez le nom de la marque: ")
        descrp = input("Entrez la description de la marque: ")

        data = (numM, nomM, descrp)
        
        cur = conn.cursor()
        cur.execute("INSERT INTO Marque VALUES (?, ?, ?)", data)
        conn.commit()
        print("Marque ajoutée avec succès")
    except sqlite3.IntegrityError as e:
        print(f"Erreur d'ajout de la marque: {e}")
    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)

def delete_marque(conn):
    pass

def update_marque(conn):
    pass


#***************************************************
# --------------------- Dossier --------------------
#***************************************************
def insert_dossier(conn):
    pass

def delete_dossier(conn):
    pass

def update_dossier(conn):
    pass


#***************************************************
# --------------------- Wishlist -------------------
#***************************************************
def insert_wishlist(conn):
    pass

def delete_wishlist(conn):
    pass

def update_wishlist(conn):
    pass


def gerer():
    database = "data/camera.db"
    conn = db.creer_connexion(database)

    if conn is not None:
        while True:
            print("1. Gérer les clients")
            print("2. Gérer les marques")
            print("3. Gérer les caméras")
            print("4. Gérer les dossiers")
            print("5. Gérer les wishlist")
            print("0. Quitter")

            choix = int(input("Entrez votre choix: "))

            if choix == 1:
                print("1. Ajouter un client")
                print("2. Supprimer un client")
                print("3. Modifier un client")
                print("0. Quitter")

                choix = int(input("Entrez votre choix: "))
                if choix == 1:
                    insert_client(conn)
                elif choix == 2:
                    delete_client(conn)
                elif choix == 3:
                    update_client(conn)
                elif choix == 0:
                    break
                else:
                    print("Choix invalide")

            elif choix == 2:
                print("1. Ajouter une marque")
                print("2. Supprimer une marque")
                print("3. Modifier une marque")
                print("0. Quitter")

                choix = int(input("Entrez votre choix: "))
                if choix == 1:
                    insert_marque(conn)
                elif choix == 2:
                    delete_marque(conn)
                elif choix == 3:
                    update_marque(conn)
                elif choix == 0:
                    break
                else:
                    print("Choix invalide")

            elif choix == 3:
                print("1. Ajouter une caméra")
                print("2. Supprimer une caméra")
                print("3. Modifier une caméra")
                print("0. Quitter")

                choix = int(input("Entrez votre choix: "))
                if choix == 1:
                    insert_camera(conn)
                elif choix == 2:
                    delete_camera(conn)
                elif choix == 3:
                    update_camera(conn)
                elif choix == 0:
                    break
                else:
                    print("Choix invalide")

            elif choix == 4:
                print("1. Ajouter un dossier")
                print("2. Supprimer un dossier")
                print("3. Modifier un dossier")
                print("0. Quitter")

                choix = int(input("Entrez votre choix: "))
                if choix == 1:
                    insert_dossier(conn)
                elif choix == 2:
                    delete_dossier(conn)
                elif choix == 3:
                    update_dossier(conn)
                elif choix == 0:
                    break
                else:
                    print("Choix invalide")

            elif choix == 5:
                print("1. Ajouter une wishlist")
                print("2. Supprimer une wishlist")
                print("3. Modifier une wishlist")
                print("0. Quitter")

                choix = int(input("Entrez votre choix: "))
                if choix == 1:
                    insert_wishlist(conn)
                elif choix == 2:
                    delete_wishlist(conn)
                elif choix == 3:
                    update_wishlist(conn)
                elif choix == 0:
                    break
                else:
                    print("Choix invalide")

    conn.close()

if __name__ == "__gerer__":
    gerer()