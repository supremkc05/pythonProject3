import random
def get_user_choice():
# Get user's choice and validate it
    user_choice = input("Enter your choice (snake, water, gun): ").lower()
    while user_choice not in ["snake", "water", "gun"]:
        print("Invalid choice. Please enter snake, water, or gun.")
        user_choice = input("Enter your choice (snake, water, gun): ").lower()
    return user_choice

def get_computer_choice():
    # Get a random choice for the computer
    return random.choice(["snake", "water", "gun"])

def determine_winner(user, computer):
    # Determine the winner based on user's and computer's choices
    if user == computer:
        return "It's a tie!"
    elif (user == "snake" and computer == "water") or (user == "water" and computer == "gun") or (user == "gun" and computer == "snake"):
        return "You win!"
    else:
        return "You lose!"

def main():
    # Main function to start the game
    print("Welcome to Snake-Water-Gun Game!")
    user_choice = get_user_choice()         # Get user's choice and validate it
    computer_choice = get_computer_choice() # Get a random choice for the computer

# Display user's and computer's choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")   # Determine the winner
    winner = determine_winner(user_choice, computer_choice)
    print(winner)

# Call the main function to start the game
main()