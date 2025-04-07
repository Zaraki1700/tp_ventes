import sqlite3
import pandas as pd

conn = sqlite3.connect('ventes_magasin.db')

# Extraction et jointure des tables
ventes_df = pd.read_sql_query("SELECT * FROM Ventes;", conn)
produits_df = pd.read_sql_query("SELECT * FROM Produits;", conn)
clients_df = pd.read_sql_query("SELECT * FROM Clients;", conn)
df_complet = pd.merge(pd.merge(ventes_df, produits_df, on="id_produit"), clients_df, on="id_client")

# Export en CSV
df_complet.to_csv("ventes_complet.csv", index=False)
conn.close()
print("✅ Données exportées dans 'ventes_complet.csv'")
