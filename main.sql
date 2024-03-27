-- Pour activer les FKs  
PRAGMA FOREIGN_KEYS=ON;
CREATE TABLE Client(
numCli INTEGER NOT NULL,
nomCli TEXT NOT NULL,
phone TEXT NOT NULL,
CONSTRAINT PK_Client PRIMARY KEY (numCli)
);

CREATE TABLE Camera(
numCam INTEGER NOT NULL,
numM INTEGER NOT NULL,
modele TEXT NOT NULL,
dateRe DATE,
qualite TEXT NOT NULL,
prix REAL NOT NULL,
CONSTRAINT PK_Camera PRIMARY KEY (numCam),
CONSTRAINT CK_Qualite CHECK (qualite IN ('parfait','correct','tresbon'))
);

CREATE TABLE Marque(
numM INTEGER NOT NULL,
nomM TEXT NOT NULL,
descrp TEXT NOT NULL,
CONSTRAINT PK_Marque PRIMARY KEY (numM)
);

CREATE TABLE Dossier(
numD INTEGER NOT NULL,
numCli INTEGER NOT NULL,
numCam INTEGER NOT NULL,
dateVente DATE,
CONSTRAINT PK_Dossier PRIMARY KEY (numD),
CONSTRAINT FK_Dossier_Client FOREIGN KEY (numCli) REFERENCES Client(numCli),
CONSTRAINT FK_Dossier_Camera FOREIGN KEY (numCam) REFERENCES Camera(numCam)
);

CREATE TABLE Wishlist(
numCli INTEGER NOT NULL,
numCam INTEGER NOT NULL,
CONSTRAINT PK_Wishlist PRIMARY KEY (numCli, numCam),
CONSTRAINT FK_Wishlist FOREIGN KEY (numCli) REFERENCES Client(numCli),
CONSTRAINT FK_Wishlist FOREIGN KEY (numCam) REFERENCES Camera(numCam)
);
