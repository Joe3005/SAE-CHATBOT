from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Charger le tokenizer et le modèle
tokenizer = AutoTokenizer.from_pretrained("Dofla/distilbert-squad")
model = AutoModelForQuestionAnswering.from_pretrained("Dofla/distilbert-squad")

def answer_question(context, question):
    # Préparer les entrées pour le modèle
    inputs = tokenizer.encode_plus(question, context, return_tensors="pt", add_special_tokens=True)
    input_ids = inputs["input_ids"]

    # Faire des prédictions avec le modèle
    outputs = model(**inputs)
    answer_start_scores = outputs.start_logits
    answer_end_scores = outputs.end_logits

    # Trouver les indices des tokens pour le début et la fin de la réponse
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1

    # Convertir les indices des tokens en string pour la réponse
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[0][answer_start:answer_end]))

    return answer
