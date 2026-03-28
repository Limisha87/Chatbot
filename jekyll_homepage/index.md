---
layout: default
title: Home
---

<h1 style="text-align:center; margin-top:50px;">Welcome to My Website</h1>
<p style="text-align:center;">This is a demo homepage content.</p>

<!-- ✅ CHAT ICON -->
<div class="chat-icon" id="chatIcon">
  <img src="/assets/icon.png" alt="chat">
</div>

<!-- ✅ CHATBOX -->
<div class="chat-container" id="chatBox">
  <div class="chat-header">TrackIn-Take Bot</div>

  <!-- Categories -->
  <div class="category-bar" id="categories"></div>

  <!-- Questions -->
  <div id="questions"></div>
</div>

<style>
.chat-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 65px;
  height: 65px;
  z-index: 999999;
  cursor: pointer;
}

.chat-icon img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

.chat-container {
  position: fixed;
  bottom: 100px;
  right: 20px;
  width: 320px;
  height: 420px;
  background: white;
  border-radius: 20px;
  display: none;
  flex-direction: column;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  overflow: hidden;
}

.chat-header {
  background: orange;
  color: white;
  padding: 12px;
  text-align: center;
  font-weight: bold;
}

.category-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  padding: 10px;
  justify-content: center;
}

.category-bar button {
  padding: 6px 12px;
  border-radius: 15px;
  border: none;
  background: #ffe0cc;
  color: #ff6600;
  cursor: pointer;
  font-size: 12px;
}

.category-bar button:hover {
  background: orange;
  color: white;
}

#questions {
  padding: 10px;
  overflow-y: auto;
  flex: 1;
  text-align: center; /* ✅ CENTER FIX */
}

.faq-item {
  text-align: left;
  margin-bottom: 8px;
}

.faq-question {
  background: #f2f2f2;
  padding: 8px;
  border-radius: 10px;
  cursor: pointer;
}

.faq-answer {
  background: #ff6600;
  color: white;
  padding: 8px;
  border-radius: 10px;
  margin-top: 5px;
  display: none;
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function () {

const chatIcon = document.getElementById("chatIcon");
const chatBox = document.getElementById("chatBox");
const categoryDiv = document.getElementById("categories");
const questionDiv = document.getElementById("questions");

let activeCategory = null;

// ✅ Categories
const categories = ["Diet","Fitness","Lifestyle","Nutrition","Veg","Non-Veg","Tools","Help"];

// ✅ FAQs
const faqs = [

  // DIET
  { category: "Diet", question: "What is diet plan?" },
  { category: "Diet", question: "How to lose weight?" },
  { category: "Diet", question: "How to gain weight?" },
  { category: "Diet", question: "What is balanced diet?" },
  { category: "Diet", question: "Best diet for beginners?" },

  // FITNESS
  { category: "Fitness", question: "Best exercise?" },
  { category: "Fitness", question: "Daily workout time?" },
  { category: "Fitness", question: "Home workout?" },
  { category: "Fitness", question: "Gym vs home?" },
  { category: "Fitness", question: "Fitness challenge?" },

  // LIFESTYLE
  { category: "Lifestyle", question: "Healthy lifestyle?" },
  { category: "Lifestyle", question: "Sleep importance?" },
  { category: "Lifestyle", question: "Daily routine?" },
  { category: "Lifestyle", question: "Stress control?" },
  { category: "Lifestyle", question: "Screen time?" },

  // NUTRITION
  { category: "Nutrition", question: "What are proteins?" },
  { category: "Nutrition", question: "What are carbohydrates?" },
  { category: "Nutrition", question: "What are fats?" },
  { category: "Nutrition", question: "What are vitamins?" },
  { category: "Nutrition", question: "What are minerals?" },
  { category: "Nutrition", question: "What is fiber?" },

  // VEG
  { category: "Veg", question: "Veg protein sources?" },
  { category: "Veg", question: "Vegetarian diet plan?" },
  { category: "Veg", question: "Veg breakfast?" },
  { category: "Veg", question: "Veg lunch?" },
  { category: "Veg", question: "Veg dinner?" },

  // NON-VEG
  { category: "Non-Veg", question: "Non-veg protein?" },
  { category: "Non-Veg", question: "Egg benefits?" },
  { category: "Non-Veg", question: "Chicken diet?" },
  { category: "Non-Veg", question: "Fish benefits?" },
  { category: "Non-Veg", question: "Dinner ideas?" },

  // TOOLS
  { category: "Tools", question: "Track water?" },
  { category: "Tools", question: "Add meals?" },
  { category: "Tools", question: "Track calories?" },
  { category: "Tools", question: "BMI calculator?" },
  { category: "Tools", question: "Progress tracking?" },

  // HELP
  { category: "Help", question: "How to login?" },
  { category: "Help", question: "How to signup?" },
  { category: "Help", question: "Forgot password?" }

];

// ✅ Toggle Chat
chatIcon.onclick = () => {
  chatBox.style.display =
    (chatBox.style.display === "flex") ? "none" : "flex";
};

// ✅ Backend call
async function fetchBotAnswer(msg, answerBox) {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: msg.toLowerCase() })
    });

    const data = await response.json();

    answerBox.innerHTML = data.answer;
    answerBox.style.display = "block";

  } catch (error) {
    answerBox.innerHTML = "Backend not connected!";
    answerBox.style.display = "block";
  }
}

// ✅ Categories render
categories.forEach(cat => {
  const btn = document.createElement("button");
  btn.textContent = cat;

  btn.onclick = () => {
    activeCategory = cat;
    renderFAQs();
  };

  categoryDiv.appendChild(btn);
});

// ✅ Questions render
function renderFAQs(){
  questionDiv.innerHTML = "";

  if(!activeCategory){
    questionDiv.innerHTML =
      "<p style='text-align:center; color:#999;'>Select category 👆</p>";
    return;
  }

  const filtered = faqs.filter(f => f.category === activeCategory);

  filtered.forEach(item => {

    const wrapper = document.createElement("div");
    wrapper.className = "faq-item";

    const q = document.createElement("div");
    q.className = "faq-question";
    q.textContent = item.question;

    const ans = document.createElement("div");
    ans.className = "faq-answer";

    q.onclick = () => {
      fetchBotAnswer(item.question, ans);
    };

    wrapper.appendChild(q);
    wrapper.appendChild(ans);
    questionDiv.appendChild(wrapper);
  });
}

// Init
renderFAQs();

});
</script>