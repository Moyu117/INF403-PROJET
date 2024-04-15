import sqlite3

conn = sqlite3.connect('data/camera.db')

# print view
def afficher_vue(conn, nom_vue):
    '''Affiche le contenu de la vue spécifiée'''

    sql = f"SELECT * FROM {nom_vue};"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

# CREATE VIEW
#--------------------------------------------
def creer_vue_client_liste(conn):
    '''Vue de la liste des clients

    affiche les informations de base sur tous les clients, y compris leur numéro, nom et numéro de téléphone.'''

    sql="""
    CREATE VIEW View_ClientList AS
    SELECT numCli, nomCli, phone
    FROM Client;"""

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Vue 'VIEW View_ClientList' créée avec succès")
    except sqlite3.Error as e:
        print(e)

#--------------------------------------------
def creer_vue_client_achat(conn):
    ''' Vue de l'historique des achats des clients

    affiche des informations détaillées sur tous les appareils photo achetés par chaque client, y compris la date d'achat, le modèle d'appareil et le prix.'''

    sql="""
    CREATE VIEW View_ClientPurchases AS
    SELECT c.numCli, c.nomCli, ca.modele, ca.qualite, ca.prix, d.dateVente
    FROM Client c
    JOIN Dossier d ON c.numCli = d.numCli JOIN Camera ca ON d.numCam = ca.numCam;"""

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Vue 'VIEW View_ClientPurchases' créée avec succès")
    except sqlite3.Error as e:
        print(e)

#--------------------------------------------
def creer_vue_appareil_achat(conn):
    ''' Vue de l'historique des achats des appareils photo

    affiche des informations détaillées sur tous les clients ayant acheté chaque appareil photo, y compris la date d'achat, le nom du client et le prix.'''

    sql="""
    CREATE VIEW View_CameraPurchases AS
    SELECT ca.numCam, ca.modele, ca.qualite, ca.prix, c.nomCli, d.dateVente
    FROM Camera ca
    JOIN Dossier d ON ca.numCam = d.numCam JOIN Client c ON d.numCli = c.numCli;"""

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Vue 'VIEW View_CameraPurchases' créée avec succès")
    except sqlite3.Error as e:
        print(e)

#--------------------------------------------
def creer_vue_vente_etat(conn):
    '''Vue d'Inventaire des caméras et état des ventes

    montre l'état de l'inventaire de tous les appareils photo et le nombre de ceux qui ont été vendus, ainsi que la date de la dernière vente pour chaque appareil'''

    sql="""
    CREATE VIEW View_CameraSalesStatus AS
    SELECT ca.numCam, ca.modele, COUNT(d.numCam) AS SalesCount, MAX(d.dateVente) AS LastSaleDate
    FROM Camera ca
    LEFT JOIN Dossier d ON ca.numCam = d.numCam
    GROUP BY ca.numCam;"""

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Vue 'VIEW View_CameraSalesStatus' créée avec succès")
    except sqlite3.Error as e:
        print(e)


# TEST
# creer_vue_client_achat(conn)
# afficher_vue(conn, 'View_ClientPurchases')

# creer_vue_appareil_achat(conn)
# afficher_vue(conn, 'View_CameraPurchases')

# creer_vue_vente_etat(conn)
# afficher_vue(conn, 'View_CameraSalesStatus')