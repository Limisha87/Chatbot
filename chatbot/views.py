from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def home(request):
    try:
        get_template('index.html')
    except TemplateDoesNotExist:
        return JsonResponse({"status": "ok", "message": "Frontend not built yet. Run npm run build."})
    return render(request, 'index.html')


def get_bot_response(message: str) -> str:
    text = message.strip().lower()
    if not text:
        return "Please type something so I can respond."
    if "hello" in text or "hi" in text:
        return "Hello! How can I help you today?"
    if "bye" in text or "goodbye" in text:
        return "Goodbye! Have a great day."
    if "how are" in text:
        return "I'm doing great, thanks! How are you?"
    if "help" in text:
        return "Sure, I can help. Tell me what you need."
    if "time" in text:
        from datetime import datetime
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"
    return "I don't fully understand yet, but I am learning!"


class ChatBotView(APIView):
    def post(self, request):
        user_message = request.data.get('message', '')
        response_text = get_bot_response(user_message)
        return Response({"response": response_text})

    def get(self, request):
        return Response({"response": "Send a POST with JSON {\"message\": \"...\"} to chat."})