import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

import json
from src import *

def main():
    # Titre de l'application
    st.header("002 - TdB de migration 2025")

    if "role" not in st.session_state:
        st.session_state.role = None
    
    ROLES = [None,"Demandeur","Réception", "Admin"]

def inscriptions():
    # Description
    st.markdown("""
    Ce tableau de bord permet de suivre l'avancement de la migration des charges vers le cloud. Vous pouvez consulter
    les progrès, les performances, et les problèmes rencontrés pendant la migration.
    """)

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

    # Bouton pour simuler la mise à jour des données
    if st.button("Mettre à jour les données de migration"):
        st.write("Données mises à jour avec succès!")


if __name__ == "__main__":
    main()
    inscription()

    
