name = "SierraBot"
age = 10
print(f"Hello, my name is {name} and I am {age} years old.")

# Dictionaries
faq = {
    "hours": "9am to 10pm", 
    "contact": "email customer service"
    }

# Lists & Loops
questions = [
    "What's your question?"
]
for question in questions:
    print(question)
    answer = input()
    if answer in faq.keys():
        print(faq[answer])
    else:
        print(f"You answered: {answer}")

print("Thank you for playing!")



# Functions
def greet(user):
    return f"Hello, {user}!"

print(greet("Sierra"))
