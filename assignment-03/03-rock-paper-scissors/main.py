import random

def get_computer_choice():
    """Returns the computer's choice randomly from rock, paper, or scissors."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game based on the rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, please try again.")
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()

    computer_choice = get_computer_choice()
    print(f"The computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
