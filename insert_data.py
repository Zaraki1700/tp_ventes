import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('ventes_magasin.db')
cursor = conn.cursor()

# Insertion des produits
produits = [
    ("Laptop", "Électronique", 999.99),
    ("T-shirt", "Vêtements", 19.99),
    ("Polo", "Vêtements", 17.66),
    ("Aspirateur", "Électroménager", 59.99),
    ("Dictionnaire", "Culture", 12.56),
    ("Smartphone", "Électronique", 699.99),
    ("Sabre", "Arme Blanche", 55.32)
]
cursor.executemany("INSERT INTO Produits (nom_produit, categorie, prix_unitaire) VALUES (?, ?, ?)", produits)

# Insertion des clients
clients = [
    ("Kenpachi Zaraki", "kenpachizaraki1700@gmail.com"),
    ("Byakuya Kuchiki", "byakuyakuchiki750@gmail.com"),
    ("Natsu Dragnir", "natsudragnir18@gmail.com"),
    ("Grey Fullbuster", "greyfullbuster18@gmail.com"),
    ("Kirua Zoldik", None),
    ("Gon Freecss", None),
    ("Goten", None),
    ("Trunks", None),
    ("Naruto Uzumaki", "narutouzumaki32@example.com"),
    ("Sasuke Uchiha", "sasukeuchiha32@gmail.com")
]
cursor.executemany("INSERT INTO Clients (nom_client, email) VALUES (?, ?)", clients)

# Insertion des ventes (100 transactions aléatoires)
for _ in range(100):
    id_produit = random.randint(1, 7)
    id_client = random.randint(1, 10)
    date_vente = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
    quantite = random.randint(1, 3)
    cursor.execute("SELECT prix_unitaire FROM Produits WHERE id_produit = ?", (id_produit,))
    prix = cursor.fetchone()[0]
    montant_total = prix * quantite
    cursor.execute("""
        INSERT INTO Ventes (id_produit, id_client, date_vente, quantite, montant_total)
        VALUES (?, ?, ?, ?, ?)
    """, (id_produit, id_client, date_vente, quantite, montant_total))

conn.commit()
conn.close()
print("✅ Données insérées avec succès dans 'ventes_magasin.db'")
