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
        "question": "Who won euro's 2024?",
        "options": ["A) Spain", "B) England", "C) Germany", "D) Netherlands"],
        "answer": "A"
    },
    {
        "question": "When was the movie Titanic released?",
        "options": ["A) 1982", "B) 1967", "C) 1997", "D) 1998"],
        "answer": "C"
    },
    # Learners can add more questions here following the same structure
]

# Score Variable
score = 0

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
        score += 1

    available_options = ["A", "B", "C", "D"]

    for option in question["options"]:
        available_options.append(option[0])

    if user_answer not in available_options:
        print (f"Incorrect option, please pick from A, B, C or D")

    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print(f"Thanks for playing the Pub Quiz! Your final score is {score} out of {len(quiz_questions)}.")