---
layout: null
---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TrackIn-Take Bot</title>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg, #fff5ec, #ffe0cc);
}

/* CHAT ICON */
.chat-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 70px;
  height: 70px;
  cursor: pointer;
  z-index: 1000;
  animation: pulse 2s infinite;
}
.chat-icon img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

/* Animation */
@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

/* CHAT BOX */
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
}

.faq-item {
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
</head>

<body>

<!-- CHAT ICON -->
<div id="chatIcon" class="chat-icon">
<img src="/Chatbot/assets/icon.png" alt="chat">
</div>

<!-- CHAT BOX -->
<div id="chatBox" class="chat-container">
  <div class="chat-header">TrackIn-Take Bot</div>

  <div id="categories" class="category-bar"></div>
  <div id="questions"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {

const chatIcon = document.getElementById("chatIcon");
const chatBox = document.getElementById("chatBox");
const categoryDiv = document.getElementById("categories");
const questionDiv = document.getElementById("questions");

let activeCategory = null;

// Toggle chat
chatIcon.addEventListener("click", function(){
    chatBox.style.display = (chatBox.style.display === "flex") ? "none" : "flex";
});

// Categories
const categories = ["Diet","Fitness","Lifestyle","Nutrition","Veg","Non-Veg","Tools","Help"];

// FAQs
const faqs = [
  { category: "Diet", question: "What is diet plan?" },
  { category: "Diet", question: "How to lose weight?" },
  { category: "Diet", question: "How to gain weight?" },
  { category: "Diet", question: "What is balanced diet?" },

  { category: "Fitness", question: "Best exercise?" },
  { category: "Fitness", question: "Daily workout time?" },

  { category: "Lifestyle", question: "Healthy lifestyle?" },
  { category: "Lifestyle", question: "Sleep importance?" },

  { category: "Nutrition", question: "What are proteins?" },
  { category: "Nutrition", question: "What are carbohydrates?" },

  { category: "Veg", question: "Veg protein sources?" },
  { category: "Non-Veg", question: "Egg benefits?" },

  { category: "Tools", question: "Track calories?" },
  { category: "Help", question: "How to login?" }
];

// Render categories
categories.forEach(cat => {
  const btn = document.createElement("button");
  btn.textContent = cat;
  btn.onclick = () => {
    activeCategory = cat;
    renderFAQs();
  };
  categoryDiv.appendChild(btn);
});

// Backend URL
const API_URL = "https://chatbot-3-3cn3.onrender.com/api/chat/";

// API call
async function sendMessage(msg, answerDiv){
    try{
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message: msg})
        });

        const data = await response.json();
        answerDiv.style.display = "block";
        answerDiv.textContent = data.answer;

    } catch(err){
        answerDiv.style.display = "block";
        answerDiv.textContent = "Backend not connected!";
    }
}

// Render FAQs
function renderFAQs(){
    questionDiv.innerHTML = "";
    if(!activeCategory) return;

    const filtered = faqs.filter(f => f.category === activeCategory);

    filtered.forEach(item => {
        const q = document.createElement("div");
        q.className = "faq-question";
        q.textContent = item.question;

        const ans = document.createElement("div");
        ans.className = "faq-answer";

        q.onclick = () => sendMessage(item.question, ans);

        questionDiv.appendChild(q);
        questionDiv.appendChild(ans);
    });
}

});
</script>

</body>
</html>