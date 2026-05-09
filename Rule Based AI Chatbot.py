responses = {
    "hello": "Hi there!",
    "hi": "Hello! How can I help you?",
    "hey": "Hey! What's up?",
    
    "how are you": "I'm just a bot, but I'm doing great!",
    "how are you doing": "All systems running perfectly!",
    
    "your name": "I'm DecodeBot, your AI assistant",
    "who are you": "I'm a rule-based AI chatbot created during an internship!",
    
    "what can you do": "I can chat with you and respond based on predefined rules.",
    
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later!",
    
    "thanks": "You're welcome!",
    "thank you": "Glad I could help!",
    
    "help": "You can ask me greetings, my name, or simple questions!",
    
    "time": "I can't check real time yet, but I'm learning!",
    "date": "I don't have date access yet, but maybe soon!",
    
    "joke": "Why did the programmer quit his job? Because he didn't get arrays",
    
    "weather": "I can't check weather yet, but it's always code weather here!",
    
    "creator": "I was created by an AI intern at DecodeLabs",
    
    "where are you from": "I live inside your computer",
    
    "do you sleep": "Nope! I run 24/7",
    
    "what is ai": "AI is the simulation of human intelligence in machines.",
    
    "what is python": "Python is a powerful programming language used in AI and more.",
    
    "motivate me": "Keep going! You're building something amazing",
    
    "tell me something": "Did you know? Python was named after Monty Python"
}



def get_response(user_input):
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I didn't understand that. Try asking something else."

print("Bot: Hello! I'm DecodeBot 🤖. Type 'exit' to quit.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    reply = get_response(user_input)
    print(f"Bot: {reply}")