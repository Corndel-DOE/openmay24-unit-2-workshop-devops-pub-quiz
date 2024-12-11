# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

score=0
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
        "question": "Who is the president of United States?",
        "options":["A) Joe Biden", "B) Donald Trump"],
        "answer":"B"
    },

    # Learners can add more questions here following the same structure
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

    available_options=[]

    for option in question["options"]:
        available_options.append(option[0])
    
    if user_answer not in available_options:
        print (f"Invalid Answer")
    else: 
        print (f"Go next")

    if user_answer == question["answer"]:
        score += 1
        print("Correct!")
       
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")
  

# Goodbye message
print(f"Thanks for playing the Pub Quiz!. You have scored {len({question['answer']})} out of {len(quiz_questions)}")



#Adding a comment to see if my commited changes shows up