from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

class QuestionAnswering(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, *args, **kwargs):
        data = request.data
        context = data.get('context_text')
        question = data.get('question')
        model_name = data.get('model_name', 'Dofla/distilbert-squad')

        if context and question:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForQuestionAnswering.from_pretrained(model_name)
            inputs = tokenizer.encode_plus(question, context, return_tensors="pt", add_special_tokens=True)
            outputs = model(**inputs)
            answer_start_scores = outputs.start_logits
            answer_end_scores = outputs.end_logits
            answer_start = torch.argmax(answer_start_scores)
            answer_end = torch.argmax(answer_end_scores) + 1
            answer = tokenizer.decode(inputs["input_ids"][0][answer_start:answer_end], skip_special_tokens=True)

            return Response({'answer': answer})
        else:
            return Response({'error': 'Context and question are required'}, status=400)
