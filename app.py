# Core pkgs
import streamlit as st



# EDA pkgs


# Data visulization pkgs



# ML pkgs

def main():

	"""Aplicación de aprendizaje automático"""

	st.title("Aplicación de aprendizaje automático")
	st.text("Exploración de datos, visualización y construcción del modelo")

	activites = ["EDA","Plot","Model Building","About"]

	choice = st.sidebar.selectbox("Seleccine el paso",activites)

if __name__ == "__main__":
    main()