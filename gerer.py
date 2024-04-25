import sqlite3
import db
import datetime

# 可改进

def valid_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def valid_price(price):
    try:
        price = float(price)
        return price > 0
    except ValueError:
        return False

#***************************************************
# --------------------- Client ---------------------
#***************************************************
def insert_client(conn): # test ok
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

def delete_client(conn): # test ok
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

def update_client(conn): # test ok
    try:
        numCli = input("Entrez le numéro du client: ")
        if not numCli.isdigit():
            print("Le numéro du client doit être un entier")
            return
        nom = input("Entrez le nom du client: ")
        phone = input("Entrez le numéro de téléphone du client: ")

        data = (numCli, nom, phone)
        
        cur = conn.cursor()
        cur.execute("UPDATE Client SET nomCli = ?, phone = ? WHERE numCli = ?", (nom, phone, numCli))
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
def insert_camera(conn): # test ok
    try:
        numCam = input("Entrez le numéro de la caméra: ")
        if not numCam.isdigit():
            print("Le numéro de la caméra doit être un entier")
            return
        numM = input("Entrez le numéro de la marque de la caméra: ")
        if not numM.isdigit():
            print("Le numéro de la marque de la caméra doit être un entier")
            return
        # check if marque exists
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM Marque WHERE numM = ?", (numM,))
        if cur.fetchone() is None:
            print("Aucune marque avec ce numéro")
            return

        modele = input("Entrez le modèle de la caméra: ")
        dateRe = input("Entrez la date de rénovation de la caméra: ")
        if not valid_date(dateRe):
            print("La date de rénovation doit être au format YYYY-MM-DD")
            return
        qualite = input("Entrez la qualité de la caméra: ")
        if qualite not in['parfait', 'correct', 'tresbon']:
            print("La qualité doit être 'parfait', 'correct' ou 'tresbon'")
            return
        prix = input("Entrez le prix de la caméra: ")
        if not valid_price(prix):
            print("Le prix doit être un nombre positif")
            return

        data = (numCam, numM, modele, dateRe, qualite, prix)
        
        cur.execute("INSERT INTO Camera VALUES (?, ?, ?, ?, ?, ?)", data)
        conn.commit()
        print("Caméra ajoutée avec succès")
    except sqlite3.IntegrityError as e:
        print(f"Erreur d'ajout de la caméra: {e}")

def delete_camera(conn): # test ok
    try:
        numCam = input("Entrez le numéro de la caméra: ")
        if not numCam.isdigit():
            print("Le numéro de la caméra doit être un entier")
            return

        data = (numCam,)
        
        cur = conn.cursor()
        cur.execute("DELETE FROM Camera WHERE numCam = ?", data)
        if cur.rowcount == 0:
            print("Aucune caméra avec ce numéro")
            return
        else:
            conn.commit()
        print("Caméra supprimée avec succès")
    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)
    

def update_camera(conn): # test ok
    try:
        numCam = input("Entrez le numéro de la caméra: ")
        if not numCam.isdigit():
            print("Le numéro de la caméra doit être un entier")
            return
        numM = input("Entrez le numéro de la marque de la caméra: ")
        if not numM.isdigit():
            print("Le numéro de la marque de la caméra doit être un entier")
            return
        # check if marque exists
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM Marque WHERE numM = ?", (numM,))
        if cur.fetchone() is None:
            print("Aucune marque avec ce numéro")
            return

        modele = input("Entrez le modèle de la caméra: ")
        dateRe = input("Entrez la date de rénovation de la caméra: ")
        qualite = input("Entrez la qualité de la caméra: ")
        prix = input("Entrez le prix de la caméra: ")

        data = (numM, modele, dateRe, qualite, prix, numCam)
        
        cur.execute("UPDATE Camera SET numM = ?, modele = ?, dateRe = ?, qualite = ?, prix = ? WHERE numCam = ?", data)
        if cur.rowcount == 0:
            print("Aucune caméra avec ce numéro")
            return
        else:
            conn.commit()
            print("Caméra mise à jour avec succès")
    except sqlite3.IntegrityError as e:
        print("Erreur de mise à jour de la caméra: ", e)


#***************************************************
# --------------------- Marque ---------------------
#***************************************************
def insert_marque(conn): # test ok
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

def delete_marque(conn): # test ok
    try:
        numM = input("Entrez le numéro de la marque: ")
        if not numM.isdigit():
            print("Le numéro de la marque doit être un entier")
            return

        data = (numM,)
        
        cur = conn.cursor()
        cur.execute("DELETE FROM Marque WHERE numM = ?", data)
        if cur.rowcount == 0:
            print("Aucune marque avec ce numéro")
            return
        else:
            conn.commit()
        print("Marque supprimée avec succès")
    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)

def update_marque(conn): # test ok
    try:
        numM = input("Entrez le numéro de la marque: ")
        if not numM.isdigit():
            print("Le numéro de la marque doit être un entier")
            return
        nomM = input("Entrez le nom de la marque: ")
        descrp = input("Entrez la description de la marque: ")

        data = (nomM, descrp, numM)
        
        cur = conn.cursor()
        cur.execute("UPDATE Marque SET nomM = ?, descrp = ? WHERE numM = ?", data)
        if cur.rowcount == 0:
            print("Aucune marque avec ce numéro")
            return
        else:
            conn.commit()
            print("Marque mise à jour avec succès")
    except sqlite3.IntegrityError as e:
        print("Erreur de mise à jour de la marque: ", e)
    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)


#***************************************************
# --------------------- Dossier --------------------
#***************************************************
def insert_dossier(conn): # test ok
    try:
        numD = input("Entrez le numéro du dossier: ")
        if not numD.isdigit():
            print("Le numéro du dossier doit être un entier")
            return
        numCli = input("Entrez le numéro du client: ")
        if not numCli.isdigit():
            print("Le numéro du client doit être un entier")
            return
        numCam = input("Entrez le numéro de la caméra: ")
        if not numCam.isdigit():
            print("Le numéro de la caméra doit être un entier")
            return
        dateVente = input("Entrez la date de vente: ")
        if not valid_date(dateVente):
            print("La date de vente doit être au format YYYY-MM-DD")
            return

        data = (numD, numCli, numCam, dateVente)
        
        cur = conn.cursor()
        # check if client and camera exist
        cur.execute("SELECT 1 FROM Client WHERE numCli = ?", (numCli,))
        if cur.fetchone() is None:
            print("Aucun client avec ce numéro")
            return
        cur.execute("SELECT 1 FROM Camera WHERE numCam = ?", (numCam,))
        if cur.fetchone() is None:
            print("Aucune caméra avec ce numéro")
            return

        cur.execute("INSERT INTO Dossier VALUES (?, ?, ?, ?)", data)
        conn.commit()
        print("Dossier ajouté avec succès")
    except sqlite3.IntegrityError as e:
        print(f"Erreur d'ajout du dossier: {e}")

def delete_dossier(conn): # test ok
    try:
        numD = input("Entrez le numéro du dossier: ")
        if not numD.isdigit():
            print("Le numéro du dossier doit être un entier")
            return

        data = (numD,)
        
        cur = conn.cursor()
        cur.execute("DELETE FROM Dossier WHERE numD = ?", data)
        if cur.rowcount == 0:
            print("Aucun dossier avec ce numéro")
            return
        else:
            conn.commit()
        print("Dossier supprimé avec succès")
    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)

def update_dossier(conn): # test ok
    try:
        numD = input("Entrez le numéro du dossier: ")
        if not numD.isdigit():
            print("Le numéro du dossier doit être un entier")
            return
        numCli = input("Entrez le numéro du client: ")
        if not numCli.isdigit():
            print("Le numéro du client doit être un entier")
            return
        numCam = input("Entrez le numéro de la caméra: ")
        if not numCam.isdigit():
            print("Le numéro de la caméra doit être un entier")
            return
        dateVente = input("Entrez la date de vente: ")

        data = (numCli, numCam, dateVente, numD)
        
        cur = conn.cursor()
        # check if client and camera exist
        cur.execute("SELECT 1 FROM Client WHERE numCli = ?", (numCli,))
        if cur.fetchone() is None:
            print("Aucun client avec ce numéro")
            return
        cur.execute("SELECT 1 FROM Camera WHERE numCam = ?", (numCam,))
        if cur.fetchone() is None:
            print("Aucune caméra avec ce numéro")
            return

        cur.execute("UPDATE Dossier SET numCli = ?, numCam = ?, dateVente = ? WHERE numD = ?", data)
        if cur.rowcount == 0:
            print("Aucun dossier avec ce numéro")
            return
        else:
            conn.commit()
            print("Dossier mis à jour avec succès")
    except sqlite3.IntegrityError as e:
        print("Erreur de mise à jour du dossier: ", e)
    except sqlite3.Error as e:
        print("Erreur de la base de données: ", e)


#***************************************************
# --------------------- Wishlist -------------------
#***************************************************
def insert_wishlist(conn):
    try:
        numCli = input("Entrez le numéro du client: ")
        numCam = input("Entrez le numéro de la caméra: ")
        
        # Check if client exists
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM Client WHERE numCli = ?", (numCli,))
        if not cur.fetchone():
            print("Le client spécifié n'existe pas.")
            return
        
        # Check if camera exists
        cur.execute("SELECT 1 FROM Camera WHERE numCam = ?", (numCam,))
        if not cur.fetchone():
            print("La caméra spécifiée n'existe pas.")
            return

        # Insert into Wishlist
        cur.execute("INSERT INTO Wishlist (numCli, numCam) VALUES (?, ?)", (numCli, numCam))
        conn.commit()
        print("Ajouté avec succès dans Wishlist.")
    except sqlite3.IntegrityError as e:
        print("Erreur lors de l'ajout à la wishlist: ", e)
    except sqlite3.Error as e:
        print("Erreur de base de données: ", e)

def delete_wishlist(conn): # test ok
    try:
        numCli = input("Entrez le numéro du client: ")
        numCam = input("Entrez le numéro de la caméra: ")
        
        cur = conn.cursor()
        cur.execute("DELETE FROM Wishlist WHERE numCli = ? AND numCam = ?", (numCli, numCam))
        if cur.rowcount == 0:
            print("Aucun élément trouvé dans la wishlist avec ces identifiants.")
            return
        
        conn.commit()
        print("Supprimé avec succès de la Wishlist.")
    except sqlite3.Error as e:
        print("Erreur de base de données: ", e)

def update_wishlist(conn): # test ok
    try:
        numCli = input("Entrez le numéro du client: ")
        numCam = input("Entrez le numéro de la caméra: ")
        
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM Wishlist WHERE numCli = ? AND numCam = ?", (numCli, numCam))
        if not cur.fetchone():
            print("Aucun élément trouvé dans la wishlist avec ces identifiants.")
            return
        
        newNumCli = input("Entrez le nouveau numéro du client: ")
        newNumCam = input("Entrez le nouveau numéro de la caméra: ")

        # Check if client exists
        cur.execute("SELECT 1 FROM Client WHERE numCli = ?", (newNumCli,))
        if not cur.fetchone():
            print("Le client spécifié n'existe pas.")
            return
        
        # Check if camera exists
        cur.execute("SELECT 1 FROM Camera WHERE numCam = ?", (newNumCam,))
        if not cur.fetchone():
            print("La caméra spécifiée n'existe pas.")
            return

        cur.execute("UPDATE Wishlist SET numCli = ?, numCam = ? WHERE numCli = ? AND numCam = ?", (newNumCli, newNumCam, numCli, numCam))
        conn.commit()
        print("Mise à jour de la wishlist réussie.")
    except sqlite3.IntegrityError as e:
        print("Erreur lors de la mise à jour de la wishlist: ", e)
    except sqlite3.Error as e:
        print("Erreur de base de données: ", e)



#-----------------------------------------------------------------------------------
def gerer():
    database = "data/camera.db"
    conn = db.creer_connexion(database)

    if conn is not None:
        while True:
            print("******************************")
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

            elif choix == 0:
                break
            else:
                print("Choix invalide")

    conn.close()

if __name__ == "__main__":
    gerer()