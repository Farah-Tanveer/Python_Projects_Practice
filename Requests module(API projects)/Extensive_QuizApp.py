import requests
import random
import html

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def fetch_questions(amount=5):
    url = f"https://opentdb.com/api.php?amount={amount}&category=18&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data['results']


num_questions = int(input("How many questions do you want? (5 or 10): "))
questions = fetch_questions(num_questions)

if len(questions) < num_questions:
    print(f"\nOnly {len(questions)} questions available from API.")
    
score = 0
for i, q in enumerate(questions[:num_questions], 1):
    print(f"\nQ{i}: {html.unescape(q['question'])}")

    options = q['incorrect_answers'] + [q['correct_answer']]
    random.shuffle(options)

    for idx, option in enumerate(options, 1):
        print(f"{idx}. {html.unescape(option)}")

    try:
        ans = int(input("Your choice (1-4): "))
        if options[ans - 1] == q['correct_answer']:
            print(f"{GREEN} Correct!{RESET}")
            score += 1
        else:
            print(f"{RED} Wrong!{RESET} Correct answer: {GREEN}{html.unescape(q['correct_answer'])}{RESET}")
    except (ValueError, IndexError):
        print(f"{RED}Invalid input!{RESET} Correct answer: {GREEN}{html.unescape(q['correct_answer'])}{RESET}")

print(f"\nYour Final Score: {score}/{num_questions}")

