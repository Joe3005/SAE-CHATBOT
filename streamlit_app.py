import streamlit as st
import requests

def format_model_name(full_name):
    # Extraire le nom après le '/' et prendre le premier mot
    short_name = full_name.split('/')[1].split('-')[0].capitalize()  # Capitalize pour améliorer l'affichage
    return short_name

# Liste des modèles avec leurs noms complets
model_names = [
    "Dofla/distilbert-squad", 
    "Dofla/roberta-base", 
    "csarron/bert-base-uncased-squad-v1"
]

# Préparation de la liste pour l'interface
model_options = [(name, format_model_name(name)) for name in model_names]

def main():
    st.title("Question Answering System")
    
    # Liste de modèles formatée pour l'affichage et la sélection
    model_options = [
        ("Dofla/distilbert-squad", "Distilbert"),
        ("Dofla/roberta-base", "Roberta"),
        ("csarron/bert-base-uncased-squad-v1", "Bert")
    ]

    # Permettre aux utilisateurs de choisir le modèle
    model_choice = st.selectbox(
        "Choose the model you want to use:",
        options=model_options,
        index=0,  # par défaut, sélectionnez le premier modèle
        format_func=lambda x: x[1]  # Utilisez le deuxième élément des tuples pour l'affichage
    )[0]  # Prendre le premier élément pour l'usage

    # Suite de votre code...

if __name__ == "__main__":
    main()
