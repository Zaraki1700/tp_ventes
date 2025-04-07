import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Dashboard Ventes", layout="wide")

# Connexion à la base SQLite
conn = sqlite3.connect('ventes_magasin.db')

# Chargement des données
@st.cache_data
def load_data():
    ventes = pd.read_sql("SELECT * FROM Ventes", conn)
    produits = pd.read_sql("SELECT * FROM Produits", conn)
    clients = pd.read_sql("SELECT * FROM Clients", conn)
    df = pd.merge(pd.merge(ventes, produits, on="id_produit"), clients, on="id_client")
    df['date_vente'] = pd.to_datetime(df['date_vente'])
    df['mois_annee'] = df['date_vente'].dt.strftime('%Y-%m')  # Conversion en string
    return df

df = load_data()

# Sidebar avec filtres
st.sidebar.header("Filtres")
categorie = st.sidebar.multiselect(
    "Catégorie produit",
    options=df['categorie'].unique(),
    default=df['categorie'].unique()
)

date_min = st.sidebar.date_input(
    "Date minimale",
    value=df['date_vente'].min()
)

# Application des filtres
df_filtered = df[
    (df['categorie'].isin(categorie)) &
    (df['date_vente'] >= pd.to_datetime(date_min))
]

# Métriques clés
st.title("📊 Tableau de bord des ventes")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("CA Total", f"{df_filtered['montant_total'].sum():,.0f} FCFA")
with col2:
    st.metric("Transactions", len(df_filtered))
with col3:
    st.metric("Panier moyen", f"{df_filtered['montant_total'].mean():,.0f} FCFA")

# Visualisations
tab1, tab2, tab3 = st.tabs(["Évolution temporelle", "Répartition", "Top clients"])

with tab1:
    # Group by mois_annee instead of Period
    monthly_sales = df_filtered.groupby('mois_annee')['montant_total'].sum().reset_index()
    fig = px.line(
        monthly_sales,
        x='mois_annee',
        y='montant_total',
        title="Évolution mensuelle du CA",
        labels={'mois_annee': 'Mois', 'montant_total': 'CA (FCFA)'}
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(
            df_filtered.groupby('categorie')['montant_total'].sum().reset_index(),
            names='categorie',
            values='montant_total',
            title="CA par catégorie"
        )
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(
            df_filtered.groupby('nom_produit')['quantite'].sum().nlargest(5).reset_index(),
            x='nom_produit',
            y='quantite',
            title="Top 5 produits"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    fig = px.bar(
        df_filtered.groupby('nom_client')['montant_total'].sum().nlargest(5).reset_index(),
        x='nom_client',
        y='montant_total',
        title="Top 5 clients"
    )
    st.plotly_chart(fig, use_container_width=True)

# Tableau détaillé
st.subheader("Données brutes")
st.dataframe(df_filtered, use_container_width=True)
