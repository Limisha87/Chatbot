from rest_framework.views import APIView
from rest_framework.response import Response


FAQ_DATA = {
    "What is diet plan?": "Diet plan helps manage daily nutrition.",
    "How to lose weight?": "Follow calorie deficit diet.",
    "How to gain weight?": "Increase calorie intake.",
    "What is balanced diet?": "Includes carbs, protein, fats, vitamins.",

    "Best exercise?": "Cardio + strength training.",
    "Daily workout time?": "At least 30 minutes.",

    "Healthy lifestyle?": "Balanced diet + sleep + exercise.",
    "Sleep importance?": "7-8 hours required.",

    "What are proteins?": "Help build muscles.",
    "What are carbohydrates?": "Provide energy.",

    "Veg protein sources?": "Paneer, dal, soyabean.",
    "Non-veg protein?": "Chicken, eggs, fish.",

    "Track water?": "Drink at least 2–3 liters daily.",
    "BMI calculator?": "Enter height & weight.",

    "How to login?": "Click login button.",
    "How to signup?": "Fill signup form."
}


# 🚀 API VIEW
class ChatBotView(APIView):

    def post(self, request):
        question = request.data.get("question", "")

        # Get answer from dictionary
        answer = FAQ_DATA.get(question, "Sorry, answer not found.")

        return Response({
            "question": question,
            "answer": answer
        })

    def get(self, request):
        return Response({
            "message": "Send POST with {question: 'your question'}"
        })