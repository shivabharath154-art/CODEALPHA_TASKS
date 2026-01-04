def chatbot():
    """A simple rule-based chatbot."""
    print("Chatbot: Hi! I'm a simple rule-based chatbot. Type 'bye' to exit.")

    
    rules= {
        "hello": "Hi!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!"
    }

   
    while True:
        
        user_input = input("You: ").lower().strip()

      
        if user_input in rules:
            response = rules[user_input]
            print(f"Chatbot: {response}")
            
           
            if user_input == "bye":
                break
        else:
            
            print("Chatbot: Sorry, I don't understand that command. I only know 'hello', 'how are you', and 'bye'.")


if __name__ == "__main__":
    chatbot()