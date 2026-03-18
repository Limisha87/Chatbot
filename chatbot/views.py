from rest_framework.decorators import api_view
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot(
    'MyBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'
)

# Corpus training
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

# Custom training
list_trainer = ListTrainer(chatbot)
list_trainer.train([
    "hi",
    "hello",
    "how are you",
    "I am fine",
    "what is your name",
    "I am a chatbot",
])


@api_view(['POST'])
def chat(request):
    try:
        user_message = request.data.get('text')

        print("User:", user_message)

        if not user_message:
            return JsonResponse({'error': 'No text provided'}, status=400)

        bot_response = chatbot.get_response(user_message)
        response_text = str(bot_response).strip()

        print("Bot:", response_text)

        if not response_text or len(response_text) < 2:
            response_text = "Sorry, I didn't understand that."

        return JsonResponse({
            'text': response_text
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)