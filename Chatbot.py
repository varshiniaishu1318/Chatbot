import random

def greet_user():
    print("Hello there! I'm your Chatbot. How can I help you today?")

def farewell_message():
    print("Goodbye! If you have more questions, feel free to return.")

def handle_basic_questions(question):
    if "your name" in question:
        return "I'm Chatbot, nice to meet you!"
    elif "your purpose" in question:
        return "I'm here to assist and make your day a bit brighter."
    elif "capabilities" in question:
        return "I can provide information, answer questions, and even tell you a joke!"
    elif "how are you" in question:
        return "I'm just a bunch of code, but I'm doing well. Thanks for asking!"
    elif "thank you" in question:
        return "You're welcome! If you need more help, just let me know."
    else:
        return None

def chat():
    greet_user()

    for _ in range(3):
        user_input = input("You: ")
        
        # Handling basic questions
        response = handle_basic_questions(user_input.lower())
        if response:
            print("Chatbot:", response)
            continue

        # Randomly choose a question from the chatbot
        questions = ["What else would you like to know?", "Any specific topic you're interested in?", "Ask me anything!"]
        chatbot_question = random.choice(questions)
        print("Chatbot:", chatbot_question)

    farewell_message()

if __name__ == "__main__":
    chat()