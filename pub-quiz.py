def print_separator():
    print("\n" + "-"*40 + "\n")

# Welcome message for the quiz
print_separator()
print("Welcome to the Pub Quiz!")
print_separator()

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
        "question": "What does 'git switch' do?",
        "options": ["A) Checks out new branch", "B) Switches off the PC", "C) Switches remote repo", "D) Git does not have such a command"],
        "answer": "A"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["A) K2", "B) Kangchenjunga", "C) Mount Everest", "D) Lhotse"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Mark Twain", "D) Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "In what year did the Titanic sink?",
        "options": ["A) 1905", "B) 1912", "C) 1923", "D) 1898"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["A) Monaco", "B) Vatican City", "C) San Marino", "D) Liechtenstein"],
        "answer": "B"
    }
]

# Initialize score
score = 0

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer with validation
    while True:
        user_answer = input("Your answer (A, B, C, D): ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

    print_separator()

# Goodbye message and score display
print("Thanks for playing the Pub Quiz!")
print(f"Your final score is {score} out of {len(quiz_questions)}.")
print_separator()
