def chatbot():
    responses = {
        "hello": "Hello there!",
        "hi": "Hello there!",
        "how are you": "I'm doing well, thanks!"
    }
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
        elif user_input == "exit":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I am still learning.")

chatbot()
