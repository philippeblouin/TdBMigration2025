import streamlit as st
import datetime

def main():
  st.write("#### Par jour")
  d = st.date_input("Quelle date voulez-vous observer?", datetime.date(2025,1,13))
  st.write("La date choisie est ",d)

  col1, col2, col3 = st.columns(3)

  col1.metric("Migration","5","+20%")
  col2.metric("Incident","9","+12%")
  col3.metric("Retour arrière","0%","0%")

if __name__ == "__main__":
  main()
