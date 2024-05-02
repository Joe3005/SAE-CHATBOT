import streamlit as st
import requests

def main():
    st.title("VIT'IA 2.0")
    
    # Utilisateur peut entrer un contexte manuellement ou charger un fichier
    context = st.text_area("Enter the text context here (optional if you upload a file):", height=200)
    uploaded_file = st.file_uploader("Or upload a text file with context", type=['txt'], key="file_uploader")

    # Si un fichier est téléchargé, utilisez ce contexte
    if uploaded_file is not None:
        file_context = str(uploaded_file.read(), 'utf-8')
        context = file_context  # Utiliser le contenu du fichier comme contexte
        st.write("Uploaded File Context (first 500 chars):", context[:500])

    question = st.text_input("Enter your question:", key="question_input")

    # Un seul bouton pour obtenir la réponse
    if st.button("Get Answer", key="get_answer_button"):
        if context and question:
            # Envoyer la requête au backend
            response = requests.post("http://localhost:8000/answer/", json={"context": context, "question": question})
            if response.status_code == 200:
                answer = response.json().get('answer')
                st.write("Answer:", answer)
            else:
                st.error("Failed to get answer from the server.")
        else:
            st.error("Please provide a context and enter a question.")

if __name__ == "__main__":
    main()
