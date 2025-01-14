import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Suivi de la Migration des Charges vers le Cloud")

# Description
st.markdown("""
Ce tableau de bord permet de suivre l'avancement de la migration des charges vers le cloud. Vous pouvez consulter
les progrès, les performances, et les problèmes rencontrés pendant la migration.
""")

# Exemple de données de migration (à remplacer par les données réelles)
data = {
    'Serveur': ['Serveur A', 'Serveur B', 'Serveur C', 'Serveur D'],
    'Statut': ['Migré', 'En cours', 'En cours', 'À migrer'],
    'Date de migration': ['2024-01-15', '2024-02-01', '2024-02-10', '2024-02-20'],
    'Progrès': [100, 50, 70, 0],
    'Coût estimé (en $)': [500, 200, 300, 0]
}

# Création d'un DataFrame avec les données
df = pd.DataFrame(data)

# Affichage du tableau des serveurs et de leur état
st.subheader("Tableau des serveurs et de l'état de la migration")
st.dataframe(df)

# Graphique de progression de la migration
st.subheader("Graphique de progression")
fig, ax = plt.subplots()
ax.bar(df['Serveur'], df['Progrès'], color=['green', 'orange', 'blue', 'red'])
ax.set_xlabel('Serveur')
ax.set_ylabel('Progrès (%)')
ax.set_title('Progrès de la migration des serveurs')
st.pyplot(fig)

# Section des alertes ou des problèmes rencontrés
st.subheader("Alertes et problèmes")
problèmes = ["Problème de performance sur le Serveur C", "Erreur de configuration sur le Serveur B"]
for problème in problèmes:
    st.markdown(f"- {problème}")

# Affichage d'une carte de l'utilisation des ressources
st.subheader("Utilisation des ressources cloud")
utilisation_resources = {
    'Ressource': ['CPU', 'Mémoire', 'Stockage'],
    'Utilisation (%)': [65, 70, 85]
}
df_resources = pd.DataFrame(utilisation_resources)

# Affichage de la carte des ressources
st.bar_chart(df_resources.set_index('Ressource'))

# Bouton pour simuler la mise à jour des données
if st.button("Mettre à jour les données de migration"):
    st.write("Données mises à jour avec succès!")