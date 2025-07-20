import random

def hangman():
    words = ["apple", "banana", "grapes", "cherry", "orange"]
    word = random.choice(words)  
    guessed = ["_"] * len(word)  
    guessed_letters = []
    attempts = 6

    print(" Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 chances. Good luck!\n")

    while attempts > 0 and "_" in guessed:
        print("Word:", " ".join(guessed))
        print("Guessed letters:", ", ".join(guessed_letters))
        print(f"Remaining attempts: {attempts}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print(" Incorrect guess.\n")
            attempts -= 1
    if "_" not in guessed:
        print(" Congratulations! You guessed the word:", word)
    else:
        print(" Game Over! The word was:", word)
hangman()
