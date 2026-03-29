---
layout: default
title: Home
---

<h1 style="text-align:center; margin-top:50px;">Welcome to TrackIn-Take Bot</h1>
<p style="text-align:center;">Select a category and click on a question to get the answer.</p>

<!-- CHAT ICON -->
<div id="chatIcon" class="chat-icon">
  <img src="/assets/icon.png" alt="chat">
</div>

<!-- CHAT CONTAINER -->
<div id="chatBox" class="chat-container">
  <div class="chat-header">TrackIn-Take Bot</div>

  <!-- Categories -->
  <div id="categories" class="category-bar"></div>

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
  cursor: pointer;
  z-index: 1000;
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
  width: 350px;
  height: 500px;
  background: white;
  border-radius: 20px;
  display: none;
  flex-direction: column;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  overflow: hidden;
  z-index: 999;
}
.chat-header {
  background: orange;
  color: white;
  text-align: center;
  padding: 12px;
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
  text-align: center;
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

// Toggle chatbox
chatIcon.addEventListener("click", function(){
    if(chatBox.style.display === "flex"){
        chatBox.style.display = "none";
    } else {
        chatBox.style.display = "flex";
    }
});

// Categories
const categories = ["Diet","Fitness","Lifestyle","Nutrition","Veg","Non-Veg","Tools","Help"];

// FAQs
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

// Render categories
categories.forEach(cat => {
  const btn = document.createElement("button");
  btn.textContent = cat;
  btn.addEventListener("click", function(){
      activeCategory = cat;
      renderFAQs();
  });
  categoryDiv.appendChild(btn);
});

// Backend call
async function sendMessage(msg, answerDiv){
    if(!msg) return;
    try{
        const response = await fetch("http://127.0.0.1:8000/api/chat/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message: msg})
        });
        const data = await response.json();
        answerDiv.style.display = "block";
        answerDiv.textContent = data.answer;
    } catch(err){
        console.error("Backend not connected!", err);
        answerDiv.style.display = "block";
        answerDiv.textContent = "Backend not connected!";
    }
}

// Render FAQs
function renderFAQs(){
    questionDiv.innerHTML = "";
    if(!activeCategory){
        questionDiv.innerHTML = "<p style='text-align:center; color:#999;'>Select category 👆</p>";
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

        q.addEventListener("click", function(){
            sendMessage(item.question, ans);
        });

        wrapper.appendChild(q);
        wrapper.appendChild(ans);
        questionDiv.appendChild(wrapper);
    });
}

// Init
renderFAQs();

});
</script>