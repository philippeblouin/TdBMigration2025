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
	st.write("#### Vue des performances")
	st.write("""
	## Par serveur
	""")
	col1, col2,col3,col4 = st.columns(4)
	col1.metric("Utilisation CPU", "56%", "+20%")
	col2.metric("Utilisation mémoire", "9%", "-12%")
	col3.metric("Utilisation stockage (libre)", "19%", "2%")
	col4.metric("Temps réponse","4 ms", "+2%")
	#style_metric_cards()


	st.write("## Par application")
	acol1, acol2= st.columns(2)
	acol1.metric("Temps réponse","2 ms","+10%")
	acol2.metric("Latences","1 ms","-0.4%")

	st.write("""
	#### Informations
	**La donnée de migration** : Correspond au volume de serveurs migrés par jour.\n
	**La donnée des incidents** : Tout événement imprévu qui perturbe ou interrompt le fonctionnement normal d'un service informatique.\n
	La progression est exprimée dans un rapport avec la valeur de la performance du jour d'avant.
	""")

if __name__ == "__main__":
	#style_metric_cards()
	main()
