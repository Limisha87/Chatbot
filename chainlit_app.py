import chainlit as cl

@cl.on_chat_start
async def main():
    await cl.send("Hello! This is Chainlit integrated with your Django chatbot.")

@cl.on_message
async def handle_message(msg: str):
    # Simple echo logic for demonstration. Replace with your actual bot API call.
    response = "You said: " + msg
    await cl.send(response)
