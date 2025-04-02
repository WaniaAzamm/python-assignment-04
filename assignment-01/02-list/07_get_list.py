def main():
    lst = []

    val = input("Enter a value (press Enter to stop): ")
    while val:
        lst.append(val)
        val = input("Enter a value (press Enter to stop): ")

    print("Here's the list:", lst)

if __name__ == '__main__':
    main()
# # This code defines a function `main` that collects user input into a list until the user presses Enter without typing anything.
