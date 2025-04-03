def main():
    print("Welcome to Mad Libs! Fill in the blanks to complete the story.")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    food = input("Enter a type of food: ")

    story = f"""
    One day, {name} went to {place}. 
    There, they saw a {adjective} {animal} that was trying to {verb}. 
    It looked so funny that {name} decided to feed it some {food}.
    The {animal} was so happy and became {name}'s best friend!
    """

    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
