import difflib

PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry, I only tell jokes."

def is_close_to_joke(user_input: str) -> bool:
    """Check if user input is similar to 'Joke' to allow minor typos."""
    return difflib.get_close_matches(user_input.lower(), ["joke"], cutoff=0.6)  

def main():
    user_input = input(PROMPT).strip() 

    if is_close_to_joke(user_input):  
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
