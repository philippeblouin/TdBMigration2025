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
import graphviz
from streamlit_extras.dataframe_explorer import dataframe_explorer

def example_one():
    dataframe = generate_fake_dataframe(
        size=500, cols="dfc", col_names=("date", "income", "person"), seed=1
    )
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)



def main():
	st.write("#### Par application")
	st.graphviz_chart('''
        digraph {
            BAK -> BBH
            BAK -> MDH
            MDH -> GDD
            GDD -> BBH
                }
					''')
	st.write("""
	### Les dépendances inter systèmes
	Plusieurs dépendances simultanées doivent être prises en compte lors de la migration des charges
	cette représentation graphique illustre la dépendance et le code de couleur associée l'est pour 
	l'état de la migration.
	""")


if __name__ == "__main__":
	main()
	#example_one()
