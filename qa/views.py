from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from qa.utils import answer_question  # Assurez-vous que cette fonction est bien définie

class QuestionAnsweringView(APIView):
    def post(self, request):
        data = request.data
        context = data.get('context')
        question = data.get('question')
        if context and question:
            answer = answer_question(context, question)
            return Response({'answer': answer})
        return Response({'error': 'Context and question are required'}, status=400)
