def read_phone_numbers():
    phonebook = {}
    while True:
        name = input("Name: ")
        if name == "":
            break
        phonebook[name] = input("Number: ")
    return phonebook

def print_phonebook(phonebook):
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        print(phonebook.get(name, f"{name} is not in the phonebook"))

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
