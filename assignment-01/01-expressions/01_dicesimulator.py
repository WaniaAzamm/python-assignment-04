import random

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Total of two dice: {total}")

def main():
    die1 = 10
    print(f"die1 in main() starts as: {die1}")
    
    roll_dice()
    roll_dice()
    roll_dice()
    
    print(f"die1 in main() is: {die1}")

if __name__ == '__main__':
    main()
# This code simulates rolling two dice and prints the total of the two dice.
