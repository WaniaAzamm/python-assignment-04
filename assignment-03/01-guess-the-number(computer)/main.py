import random

def computer_guess():
    print("Welcome! Think of a number between 1 and 100, and I will try to guess it!")
    
    low = 1
    high = 100
    feedback = ''
    
    while feedback != 'c':
        if low > high:
            print("Oops! There seems to be an error in the range. Let's try again.")
            break
        
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter only 'H', 'L', or 'C'.")
    
    if feedback == 'c':
        print(f"Yay! I guessed your number {guess}. Thanks for playing!")

computer_guess()
