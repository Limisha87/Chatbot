// async function sendMessage() {
//     let input = document.getElementById("userInput");
//     let message = input.value;

//     if (message.trim() === "") return;

//     let chatBox = document.getElementById("chatBox");

//     // User message
//     chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;

//     input.value = "";

//     try {
//         let response = await fetch("/api/chat/", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({ message: message })
//         });

//         let data = await response.json();

//         // Bot response
//         chatBox.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;
//         chatBox.scrollTop = chatBox.scrollHeight;

//     } catch (error) {
//         chatBox.innerHTML += `<p class="text-red-500">Server error</p>`;
//     }
// }