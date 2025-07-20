def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    responses = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "hey": "Hey!",
        "how are you": "I'm doing well, thanks for asking!",
        "what's your name": "I'm ChatBot, your simple assistant.",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "See you soon!",
        "thank you": "You're welcome!",
        "thanks": "No problem!",
        "what can you do": "I can chat with you and answer simple questions.",
        "help": "You can say hello, ask how I am, or say bye to end the chat."
    }
    return responses.get(user_input, "Sorry, I didn't understand that.")

def chatbot():
    print("Welcome to ChatBot!")
    print("Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye!")
            break

        response = get_bot_response(user_input)
        print("Bot:", response)

chatbot()

