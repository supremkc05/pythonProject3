import random

def choose_word():
    words = ["python", "java", "c++", "javascript", "ruby"]
    return random.choice(words)

def display_word(word, guess_letters):
    display = ""
    for letter in word:
        if letter in guess_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman")
    secret_word = choose_word().lower()
    guess_letters = []
    max_attempts = 6
    attempts = 0
    
    while attempts < max_attempts:
        current_display = display_word(secret_word, guess_letters)
        print(f"\nCurrent word: {current_display}")

        guess = input("Guess a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guess_letters:
            print("You already guessed that letter. Try again.")
            continue

        guess_letters.append(guess)

        if guess not in secret_word:
            attempts += 1
            print(f"Wrong guess! Attempts remaining: {max_attempts - attempts}")

        if "_" not in display_word(secret_word, guess_letters):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

    if "_" in display_word(secret_word, guess_letters):
        print(f"Sorry, you ran out of attempts. The word was: {secret_word}")


hangman()
