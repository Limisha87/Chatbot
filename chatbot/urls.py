from django.urls import path
from .views import chat

urlpatterns = [
    path('chat/', chat),
    # path('api/chat/', ChatBotApiView.as_view(), name='chatbot_api'),
]


