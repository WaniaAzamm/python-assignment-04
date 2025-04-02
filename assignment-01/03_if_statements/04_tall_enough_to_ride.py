MINIMUM_HEIGHT = 5.7  # Minimum height in feet

def main():
    while True:
        height = input("How tall are you? (Press Enter to quit) ")

        if height == "":
            break
        
        if height.isdigit():
            height = int(height)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    main()
