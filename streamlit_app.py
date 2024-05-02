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
    
    # Zone de texte pour entrer le contexte manuellement
    context = st.text_area("Or enter text context here:", height=200)

    # Chargeur de fichiers pour le contexte
    uploaded_file = st.file_uploader("Upload a text file with context (optional)", type=['txt'])

    # Déterminer la source du contexte
    if uploaded_file is not None:
        # Lire le fichier et l'utiliser comme contexte
        context = str(uploaded_file.read(), "utf-8")
        st.write("Uploaded File Context (first 500 chars):", context[:500])

    question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if context and question:
            # Envoyer la requête au backend
            response = requests.post(
                "http://localhost:8000/answer/",
                json={
                    "context_text": context,
                    "question": question,
                    "model_name": model_choice
                }
            )
            if response.status_code == 200:
                answer = response.json().get('answer')
                st.write("Answer:", answer)
            else:
                st.error("Failed to get answer from the server.")
        else:
            st.error("Please provide a context and enter a question.")

if __name__ == "__main__":
    main()
