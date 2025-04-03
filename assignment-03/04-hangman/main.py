import random

def choose_word():
    """Randomly selects a word from a list of words."""
    words = ['python', 'hangman', 'developer', 'programming', 'challenge']
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the word with underscores for unguessed letters."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    """Main function to play Hangman."""
    print("Welcome to Hangman!")
    
    word = choose_word()  
    guessed_letters = [] 
    incorrect_guesses = 0 
    max_incorrect_guesses = 6  

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

play_game()
