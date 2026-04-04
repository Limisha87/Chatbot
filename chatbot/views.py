# chatbot/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class MenuView(APIView):
    def get(self, request):
        return Response({"message": "Menu working"})
    
# MENU DATA
# ---------------------------
MENU_DATA = {
    "About TrackIntake": "TrackIntake is an AI-powered nutrition and health tracking platform that helps you log your daily meals, monitor your nutrition, and receive personalized diet recommendations.",
    "Data & Security": "Your data is safe, secure, and never shared without your permission.",
    "Contact Us": "📞 7898622813"
}

# ---------------------------
# USER FAQ
# ---------------------------
USERSECTIONS = {

    "How to Use": [
        {"q": "How do I start using TrackIntake?", "a": "Create an account, complete your profile, and start logging your meals."},
        {"q": "What details are required first?", "a": "Enter age, weight, height, and your health goals."},
        {"q": "Is it easy for beginners?", "a": "Yes, the platform is simple and user-friendly."},
        {"q": "Do I need to use it daily?", "a": "Daily usage improves tracking accuracy."},
        {"q": "Can I skip profile setup?", "a": "Yes, but completing profile gives better recommendations."}
    ],

    "Track Meals": [
        {"q": "How do I log my meals?", "a": "Enter food items and calories will be calculated automatically."},
        {"q": "Can I edit my meals later?", "a": "Yes, you can edit or delete entries anytime."},
        {"q": "How are meals organized?", "a": "Meals are divided into breakfast, lunch, dinner, and snacks."},
        {"q": "Does it support Indian food?", "a": "Yes, many Indian foods are supported."},
        {"q": "Is there a food search option?", "a": "Search feature may be limited but improving."}
    ],

    "Diet Plans": [
        {"q": "How do I get diet plans?", "a": "Plans are generated based on your profile."},
        {"q": "Are diet plans personalized?", "a": "Yes, based on your data."},
        {"q": "Can I follow plans without a nutritionist?", "a": "Yes, but expert advice helps."},
        {"q": "Will veg preference be followed?", "a": "System tries to follow your preference."},
        {"q": "Are diet plans accurate?", "a": "Based on standard nutrition data."}
    ],

    "Health Tracking": [
        {"q": "What health tools are available?", "a": "BMI, water tracker, and weight tracking."},
        {"q": "Can I track my BMI?", "a": "Yes, by entering height and weight."},
        {"q": "Can I track water intake?", "a": "Yes, daily tracking available."},
        {"q": "Can I track my weight?", "a": "Yes, monitor progress easily."},
        {"q": "Is this platform suitable for diabetes or heart patients?", "a": "Yes, TrackIntake supports diabetes, heart health, and lifestyle conditions."}
    ],

    "My Progress": [
        {"q": "Can I see my progress?", "a": "Yes, on dashboard."},
        {"q": "What does dashboard show?", "a": "Calories, water intake, and weight summary."},
        {"q": "Can I track long-term progress?", "a": "Yes, trends available."},
        {"q": "Does it help motivation?", "a": "Yes, helps consistency."},
        {"q": "Is progress tracking automatic?", "a": "Yes."}
    ],

    
    "Help & Support": [
        {"q": "Can I contact support?", "a": "Yes."},
        {"q": "Can I consult nutritionist?", "a": "Yes."},
        {"q": "What if I face issues?", "a": "Contact support."},
        {"q": "Is help available anytime?", "a": "Depends on support."},
        {"q": "Can I give feedback?", "a": "Yes."}
    ]
}

# ---------------------------
# NUTRITIONIST FAQ
# ---------------------------
NUTRITIONSECTIONS = {

    "Patients": [
        {"q": "Can I manage multiple patients?", "a": "Yes, manage multiple patients easily."},
        {"q": "Can I monitor patients daily?", "a": "Yes, track daily progress."},
        {"q": "Can I get new patients?", "a": "Yes, platform helps connect."},
        {"q": "How to track progress?", "a": "Use dashboard reports."},
        {"q": "Is patient data easy?", "a": "Yes, organized properly."}
    ],

    "Diet Plans": [
        {"q": "How to create plans?", "a": "Use templates and AI suggestions."},
        {"q": "Can I customize?", "a": "Yes."},
        {"q": "Indian diet support?", "a": "Yes."},
        {"q": "Reuse plans?", "a": "Yes."},
        {"q": "AI help?", "a": "Yes."}
    ],

    "Consultations": [
        {"q": "Online consultation?", "a": "Yes."},
        {"q": "Easy communication?", "a": "Yes."},
        {"q": "Schedule sessions?", "a": "Yes."},
        {"q": "Follow-up support?", "a": "Yes."},
        {"q": "Convenient?", "a": "Yes."}
    ],

    "Earnings": [
        {"q": "How to earn?", "a": "Through services."},
        {"q": "Multiple options?", "a": "Yes."},
        {"q": "Set pricing?", "a": "Yes."},
        {"q": "Grow practice?", "a": "Yes."},
        {"q": "Track income?", "a": "Yes."}
    ],

    "Help & Support": [
        {"q": "Facing issues?", "a": "Contact support."},
        {"q": "Technical support?", "a": "Yes."},
        {"q": "Demo available?", "a": "Yes."},
        {"q": "Contact?", "a": "Email or support."},
        {"q": "Feedback?", "a": "Yes."}
    ]
}

# ---------------------------
# API VIEW
# ---------------------------
@method_decorator(csrf_exempt, name='dispatch')
class ChatBotView(APIView):

    def get(self, request):
        return Response({"message": "Use POST method"})

    def post(self, request):
        try:
            question = request.data.get("question", "").lower().strip()

            # combine all FAQs
            all_data = []

            for section in USERSECTIONS.values():
                all_data.extend(section)

            for section in NUTRITIONSECTIONS.values():
                all_data.extend(section)

            # find answer
            for item in all_data:
                if item["q"].lower().strip() == question:
                    return Response({
                        "answer": item["a"]
                    })

            return Response({
                "answer": "Answer not found"
            })

        except Exception as e:
            return Response({
                "answer": "Server error",
                "error": str(e)
            })