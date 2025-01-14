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
La page est prise en charge par la plateforme Streamlit et elle est interprétée lors du chargement par le fureteur web.
"""
import streamlit as st
#import graphviz
#import streamlit-extras
#from streamlit_extras.metric_cards import style_metric_cards
import datetime

def main():
	st.write("#### Par jour")
	d = st.date_input("Quelle date voulez vous observer", datetime.date(2025, 1, 6))
	st.write("La date de migration choisie :", d)
	# Create a graphlib graph object

	col1, col2, col3 = st.columns(3)
	col1.metric("Migration", "5", "+20%")
	col2.metric("Incident", "9", "-12%")
	col3.metric("Retour arrière", "0%", "0%")
	#style_metric_cards()

	st.write("""
	#### Informations
	**La donnée de migration** : Correspond au volume de serveurs migrés par jour.\n
	**La donnée des incidents** : Tout événement imprévu qui perturbe ou interrompt le fonctionnement normal d'un service informatique.\n
	**La donnée de retour arrière** : Mesure d'urgence à mettre en oeuvre lorsque le rétablissement du service dépasse anormalememnt les délais prévus.\n
	\n
	La progression est exprimée dans un rapport avec la valeur de la performance du jour d'avant.
	""")

if __name__ == "__main__":
	#style_metric_cards()
	main()
