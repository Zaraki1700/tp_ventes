import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventes_complet.csv")
df['date_vente'] = pd.to_datetime(df['date_vente'])

# Graphique 1 : Évolution mensuelle du CA
df['mois'] = df['date_vente'].dt.to_period('M')
ca_mensuel = df.groupby('mois')['montant_total'].sum()
ca_mensuel.plot(kind='line', title="Chiffre d'affaires mensuel", xlabel="Mois", ylabel="CA (FCFA)")
plt.savefig("evolution_ca.png")  # Sauvegarde en image
plt.close()  # Ferme la figure pour libérer la mémoire

# Graphique 2 : Répartition des ventes par produit
ca_par_produit = df.groupby('nom_produit')['montant_total'].sum()
ca_par_produit.plot(kind='pie', autopct='%1.1f%%', title="Répartition du CA par produit")
plt.savefig("repartition_produits.png")
plt.close()

print("✅ Graphiques sauvegardés : 'evolution_ca.png' et 'repartition_produits.png'")
