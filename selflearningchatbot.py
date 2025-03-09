import re
context = None
def chatbot_response(user_input):
    global context 
    user_input = user_input.lower() 
    if re.search(r"\b(hello|hi|hey)\b", user_input):
        context = None  t
        return "Hello! How can I assist you today?"
    elif re.search(r"your name", user_input):
        context = None 
        return "I'm ChatBot, here to help with your queries!"
    elif re.search(r"(weather|temperature)", user_input):
        context = None  
        return "I'm not equipped to provide weather updates, but I recommend checking your favorite weather app!"
    elif "book" in user_input:
        context = "book"  
        return "What type of book are you looking for? (e.g., fiction, non-fiction, self-help)"
    elif context == "book" and re.search(r"(fiction|non-fiction|self-help)", user_input):
        context = None 
        if "fiction" in user_input:
            return "I recommend 'To Kill a Mockingbird' by Harper Lee."
        elif "non-fiction" in user_input:
            return "You might enjoy 'Sapiens: A Brief History of Humankind' by Yuval Noah Harari."
        elif "self-help" in user_input:
            return "Try 'Atomic Habits' by James Clear for some great insights."
    elif re.search(r"\b(bye|exit|goodbye)\b", user_input):
        context = None 
        return "Goodbye! Have a wonderful day!"
    else:
        context = None  
        return "I'm sorry, I didn't understand that. Could you please rephrase or ask something else?"
print("ChatBot: Hi there! Feel free to ask me anything. Type 'bye' to exit the conversation.")
while True:
    user_input = input("You: ")
    if re.search(r"\b(bye|exit|goodbye)\b", user_input.lower()):
        print("ChatBot: Goodbye! Take care!")
        break
    print(f"ChatBot: {chatbot_response(user_input)}")
