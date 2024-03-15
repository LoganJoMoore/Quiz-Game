
questions = [
    {
        "prompt": "What is the capital of the United States?",
        "options": ["A. Paris", "B. London", "C. Washington D.C.", "D. Madrid"],
        "answer": "C"
    },
    {
        "prompt": "What is the primary language of Brazil?",
        "options": ["A. Spanish", "B. English", "C. French", "D. Portugese"],
        "answer": "D"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 5", "D. 0"],
        "answer": "B"
    },
    {
        "prompt": "Who is the author of the Harry Potter series?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "C"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ")
        if answer.upper() == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer was", question["answer"], "\n")

    print(f"You got {score} out of {len(questions)} questions correct!")

run_quiz(questions)