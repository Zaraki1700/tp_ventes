import pandas as pd

df = pd.read_csv("ventes_complet.csv")

# Chiffre d'affaires total
ca_total = df['montant_total'].sum()
print(f"💰 Chiffre d'affaires total : {ca_total:.2f} FCFA")

# Top 5 des produits par quantité
top_produits = df.groupby('nom_produit')['quantite'].sum().nlargest(5)
print("\n🏆 Top 5 des produits par quantité vendue :\n", top_produits)

# Panier moyen
panier_moyen = df['montant_total'].mean()
print(f"\n🛒 Panier moyen : {panier_moyen:.2f} FCFA")
