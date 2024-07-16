# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "B"
    },
    {
        "question": "What colour is the sky?",
        "options": ["A) Green", "B) Yellow", "C) Blue", "D) The sky is communist propaganda"],
        "answer": "C"
    },
    {
        "question": "Which country won the Euros 2024 football championship?",
        "options": ["A) England LOL", "B) Brazil", "C) Netherlands", "D) Spain"],
        "answer": "D"
    },
    {
        "question": "If Johnny has 87 watermelons, is he: ",
        "options": ["A) Hungry", "B) Crazy", "C) Hydrated", "D) A collector"],
        "answer": "B"
    },
    {
        "question": "What is '2' + '2'?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "D"
    },
]

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print("Thanks for playing the Pub Quiz!")
