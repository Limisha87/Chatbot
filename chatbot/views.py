from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


VALID_QUESTIONS = {
    # Diet
    "what is diet plan?": "Diet plan helps manage daily nutrition.",
    "how to lose weight?": "Follow a calorie deficit diet.",
    "how to gain weight?": "Increase calorie intake gradually.",
    "what is balanced diet?": "Includes carbs, protein, fats, vitamins.",
    "best diet for beginners?": "Start with simple home-cooked meals.",

    # Fitness
    "best exercise?": "Cardio + strength training.",
    "daily workout time?": "At least 30 minutes a day.",
    "home workout?": "Pushups, squats, yoga.",
    "gym vs home?": "Both are effective if consistent.",
    "fitness challenge?": "A plan to improve fitness over time.",

    # Lifestyle
    "healthy lifestyle?": "Balanced diet + sleep + exercise.",
    "sleep importance?": "7-8 hours of sleep daily is recommended.",
    "daily routine?": "Wake up early and stay active.",
    "stress control?": "Meditation, exercise, and breaks help.",
    "screen time?": "Limit usage to avoid eye strain.",

    # Nutrition
    "what are proteins?": "Help build muscles and repair tissues.",
    "what are carbohydrates?": "Provide energy for the body.",
    "what are fats?": "Energy storage and hormone regulation.",
    "what are vitamins?": "Boost immunity and overall health.",
    "what are minerals?": "Support body functions like bones and nerves.",
    "what is fiber?": "Improves digestion and gut health.",

    # Veg
    "veg protein sources?": "Paneer, dal, soyabean, legumes.",
    "vegetarian diet plan?": "Include fruits, vegetables, grains, and protein.",
    "veg breakfast?": "Oats, fruits, milk, or yogurt.",
    "veg lunch?": "Roti, sabzi, dal, rice.",
    "veg dinner?": "Light khichdi or salad.",

    # Non-Veg
    "non-veg protein?": "Chicken, eggs, fish.",
    "egg benefits?": "High protein and rich in nutrients.",
    "chicken diet?": "Lean protein source for muscle gain.",
    "fish benefits?": "Rich in Omega-3 fatty acids.",
    "dinner ideas?": "Grilled chicken or fish with veggies.",

    # Tools
    "track water?": "Use a water tracker to log daily intake.",
    "add meals?": "Use the dashboard to log meals.",
    "track calories?": "Enter food details to monitor calories.",
    "bmi calculator?": "Enter height & weight to calculate BMI.",
    "progress tracking?": "Check reports to monitor progress.",

    # Help
    "how to login?": "Click the login button and enter credentials.",
    "how to signup?": "Fill the signup form with required details.",
    "forgot password?": "Use the reset password option on login page."
}

@method_decorator(csrf_exempt, name='dispatch')
class ChatBotView(APIView):
    def post(self, request):
        question = request.data.get("question", "").strip().lower()

        if not question:
            return Response({
                "question": "",
                "answer": "Please ask a valid question."
            })

        # Look up the answer in VALID_QUESTIONS
        answer = VALID_QUESTIONS.get(question.lower().strip())
        return Response({
            "question": question,
            "answer": answer
        })
