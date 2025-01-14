#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Script de Tableau de bord
-------------------------

Description :
Ce script permet de présenter un tableau de bord qui répond aux critères
du dossier d'analyses.

Auteur :
--------
Philippe Blouin, partenaires, philippe.blouin2@partenaires.mapaq.qc.ca
418 803-2734

Version:
--------
1.0.5

Dépendances :
-------------
Streamlit,
Streamlit-Extras

Exécution :
------------
Pour exécuter ce script utilisez le terminal,
<répertoire source>% streamlit run Tableau_de_bord.py

"""
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

st.header("TdB de migration 2025")

# Gestion par rôle
# L'attribut 'role' n'existe pas. Il faut le créé.
if "role" not in st.session_state:
	st.session_state.role = None

ROLES = [None,"Demandeur","Réception","Admin"]

def login():
	st.header("Log In")
	role = st.selectbox("Choisi un rôle",ROLES)
	if st.button("Login"):
		st.session_state.role=role
		st.rerun()

def logout():
	st.session_state.role = None
	st.rerun()

def main():
	#st.write(f"Vous êtes connecté en tant que {st.session_state.role}.")
	etat = st.session_state
	print(etat)
	col1.write("\n")
	col1.metric("Nombre de serveurs cloud actif","244","+25")
	col1.metric("Nombre de serveurs cloud inactif","(54)","-25")
	col1.metric("Budget actif","82 223$ /123 211$","66%")
	col1.write("""depuis le 10 janvier 2025""")
	col2.write("#### Bienvenue sur le tableau de bord du suivi de la migration")
	col2.write("Ce tableau de bord a été conçu pour offrir une vue d'ensemble en temps quasi réel de l'avancement de la migration des charges de traitements dans le cloud. Il permet de suivre les étapes clés du projet, d'identifier les éventuels retards ou blocage, et de faciliter la prise de décision grâce à une présentation claire des indicateurs.")
	col2.metric("Nombre d'incident","9","-12%")

	st.write("### Sources de données")
	st.write("Les informations affichées dans le tableau de bord proviennent des sources suivantes : ")
	st.write("\t**Système de gestion de projet** : Statut des charges de traitement.")
	st.write("\t**Outils de surveillance**: Statistique en temps quasi réel sur les serveurs migrés.")

#Résumé
#"""
#Résumé:
#-------
#Ce script lance la première page du Streamlit. La première page possède le nom
#du script python lancé.
#
#Prochaines étapes :
#-------------------
#Connexion sur les sources de données et rendre dynamique (heure)
#Connexion sur les sources de données autres.
#
#Notes supplémentaires :
#-----------------------
#Aucune
#"""
if __name__ == "__main__":
	col1, col2 = st.columns(2)
	style_metric_cards()
	main()