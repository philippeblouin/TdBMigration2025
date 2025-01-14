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
import datetime

def main():
	st.header("Par serveur")
	col1, col2 = st.columns(2)
	col1.write("""
	Liste des serveurs constituant actuellement la vague de migration (**FQDN**)\n
	---\n
	qubc1-appll01X.mapaq.ministere.labo\n	
	qubc1-appll02X.mapaq.ministere.labo\n
	qubc1-appll03X.mapaq.ministere.labo\n
	""")
	col2.write("""
	Quam ob rem vita quidem talis fuit vel fortuna vel gloria, ut nihil posset accedere, moriendi autem sensum celeritas abstulit; quo de genere mortis difficile dictu est; quid homines suspicentur, videtis; hoc vere tamen licet dicere, P. Scipioni ex multis diebus, quos in vita celeberrimos laetissimosque viderit, illum diem clarissimum fuisse, cum senatu dimisso domum reductus ad vesperum est a patribus conscriptis, populo Romano, sociis et Latinis, pridie quam excessit e vita, ut ex tam alto dignitatis gradu ad superos videatur deos potius quam ad inferos pervenisse.
	""")
if __name__ == "__main__":
	main()

