import random

# Python Question Bank
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": ["a) func", "b) define", "c) def", "d) function"],
        "answer": "c"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "choices": ["a) .py", "b) .pt", "c) .pyt", "d) .python"],
        "answer": "a"
    },
    {
        "question": "How do you write a comment in Python?",
        "choices": ["a) // comment", "b) <!-- comment -->", "c) # comment", "d) /* comment */"],
        "answer": "c"
    },
    {
        "question": "Which data type is immutable in Python?",
        "choices": ["a) List", "b) Dictionary", "c) Set", "d) Tuple"],
        "answer": "d"
    },
    {
        "question": "What will 3 * 'Hi' output?",
        "choices": ["a) 9", "b) HiHiHi", "c) Error", "d) Hi*3"],
        "answer": "b"
    },
    {
        "question": "Which function is used to get input from the user?",
        "choices": ["a) get()", "b) input()", "c) read()", "d) scan()"],
        "answer": "b"
    },
    {
        "question": "What is the output of len([1,2,3])?",
        "choices": ["a) 2", "b) 3", "c) [1,2,3]", "d) Error"],
        "answer": "b"
    },
    {
        "question": "Which of these is used to define a block of code in Python?",
        "choices": ["a) Braces {}", "b) Parentheses ()", "c) Indentation", "d) Quotes ''"],
        "answer": "c"
    },
    {
        "question": "Which of the following is a Python loop?",
        "choices": ["a) do-while", "b) for", "c) repeat-until", "d) switch"],
        "answer": "b"
    },
    {
        "question": "What is the correct way to declare a variable in Python?",
        "choices": ["a) int x = 5", "b) var x = 5", "c) x = 5", "d) declare x = 5"],
        "answer": "c"
    }
]
random.shuffle(questions)

score = 0
total_questions = 5  

print("Welcome to the Python Quiz!\n")
for i in range(total_questions):
    q = questions[i]
    print(f"Q{i+1}: {q['question']}")
    for choice in q["choices"]:
        print(choice)

    user_answer = input("Your answer (a/b/c/d): ").lower()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {q['answer']}\n")

print(f"Quiz Over! You got {score} out of {total_questions} correct.")
