import random

def get_user_choice():
    user_choice = input("Enter your choice (snake, water, gun): ").lower()
    while user_choice not in ["snake", "water", "gun"]:
        print("Invalid choice. Please enter snake, water, or gun.")
        user_choice = input("Enter your choice (snake, water, gun): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["snake", "water", "gun"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "snake" and computer == "water") or (user == "water" and computer == "gun") or (user == "gun" and computer == "snake"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Snake-Water-Gun Game!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
