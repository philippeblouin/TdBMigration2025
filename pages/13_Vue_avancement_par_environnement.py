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
import pandas as pd
import numpy as np
#from streamlit_extras.metric_cards import style_metric_cards

def main():
	col1.write("#### Par environnement")
	col1.write("##### Graphique de progression de la migration")
	chart_data = pd.DataFrame(np.random.randn(5, 3), columns=["Laboratoire", "Développement/Accpt", "Production"])
	col2.line_chart(chart_data)
	col1.write("""
	Quam ob rem vita quidem talis fuit vel fortuna vel gloria, ut nihil posset accedere, moriendi autem sensum celeritas abstulit; quo de genere mortis difficile dictu est; quid homines suspicentur, videtis; hoc vere tamen licet dicere, P. Scipioni ex multis diebus, quos in vita celeberrimos laetissimosque viderit, illum diem clarissimum fuisse, cum senatu dimisso domum reductus ad vesperum est a patribus conscriptis, populo Romano, sociis et Latinis, pridie quam excessit e vita, ut ex tam alto dignitatis gradu ad superos videatur deos potius quam ad inferos pervenisse.
	""")
	st.write("### Nombre de serveurs actifs par environnement")
	m1,m2,m3,m4 = st.columns(4)
	m1.metric("Production","123/432","10%")
	m2.metric("Acceptation","122/221","2%")
	m3.metric("Développement","44/89","10%")
	m4.metric("Laboratoire","122/332","22%")
if __name__ == "__main__":
	col1,col2 = st.columns(2)
	main()
