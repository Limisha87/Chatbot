from rest_framework.views import APIView
from rest_framework.response import Response
from chatterbot import ChatBot

chatbot = ChatBot(
    'MyBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3',
    read_only=True,
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
    ]
)

class ChatBotView(APIView):
    def post(self, request):
        user_message = request.data.get('message')
        if not user_message:
            return Response({"error": "Message is required."}, status=400)

        response = chatbot.get_response(user_message)
        return Response({"response": str(response)})