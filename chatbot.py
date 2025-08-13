import json

def load_faqs():
    try:
        with open("data/faqs.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Create default FAQ data if file doesn't exist
        default_faqs = {
            "faqs": [
                {
                    "id": 1,
                    "question": "How do I get started?",
                    "answer": "To get started, run 'python src/sierra_agent/cli.py' from the sierra-starter-agent directory.",
                    "category": "Getting Started"
                },
                {
                    "id": 2,
                    "question": "What is Sierra Agent?",
                    "answer": "Sierra Agent is an AI assistant designed to help you learn and work with code. It provides interactive guidance and answers to common questions.",
                    "category": "General"
                }
            ]
        }
        return default_faqs

def get_answer(user_input):
    try:
        faqs = load_faqs()["faqs"]
        
        # Check for exact question matches
        for faq in faqs:
            if faq["question"].lower() == user_input.lower():
                return faq["answer"]
        
        # Check for partial matches
        for faq in faqs:
            if user_input.lower() in faq["question"].lower():
                return f"Found a similar question: {faq['question']}\nAnswer: {faq['answer']}"
        
        # Check for help commands
        if user_input.lower() in ["help", "what questions can you answer?", "list questions"]:
            questions = [faq["question"] for faq in faqs]
            return "I can answer these questions:\n" + "\n".join(f"- {q}" for q in questions)
        
        return "I don't know the answer to that question. Try asking 'help' to see what I can answer."
        
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

def main():
    print("Welcome to the Sierra Agent! How can I help you today?")
    print("Type 'help' to see available questions, or 'exit' to quit.")
    
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == "exit":
                print("Thank you for using the Sierra Agent! Goodbye!")
                break
            
            answer = get_answer(user_input)
            print(answer)
            
        except KeyboardInterrupt:
            print("\n\nThank you for using the Sierra Agent! Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()