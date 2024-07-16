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
        "question": "Who won the last football world cup?",
        "options": ["A) England", "B) Spain", "C) Germany", "D) South Africa"],
        "answer": "B"
    },
    {
        "question": "What is prince harrys' wifes' name?",
        "options": ["A) Meghan", "B) Abigail ", "C) Gertrude", "D) Joan"],
        "answer": "A"
    },

    # Learners can add more questions here following the same structure
]

# Keep Track of Score

# Initialize score variable
score = 0

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)

    # Get the user answer with Validation
    while True:
        user_answer = input("Your answer (A, B, C, D): ").strip().upper()  # Ensuring the input is uppercase for comparison
        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid answer, please select A,B,C, or D. (Must be UpperCase)")

    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1  # Increment the score for a correct answer
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print(f"Thanks for playing the Pub Quiz! Your final score is {score} out of {len(quiz_questions)}")
