CREATE TABLE Produits (
    id_produit INTEGER PRIMARY KEY,
    nom_produit TEXT NOT NULL,
    categorie TEXT,
    prix_unitaire REAL
);

CREATE TABLE Clients (
    id_client INTEGER PRIMARY KEY,
    nom_client TEXT NOT NULL,
    email TEXT
);

CREATE TABLE Ventes (
    id_vente INTEGER PRIMARY KEY,
    id_produit INTEGER,
    id_client INTEGER,
    date_vente TEXT,
    quantite INTEGER,
    montant_total REAL,
    FOREIGN KEY (id_produit) REFERENCES Produits(id_produit),
    FOREIGN KEY (id_client) REFERENCES Clients(id_client)
);
