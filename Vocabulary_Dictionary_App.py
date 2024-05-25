dictionary = {
    "programming": "Writing instructions and commands for the computer using programming languages.",
    "computer": "An electronic device used for processing data.",
    "internet": "A global network connecting millions of smaller networks.",
}

def find_meaning(word):
    return dictionary.get(word, "Word not found in the dictionary.")

def add_word(word, meaning):
    dictionary[word] = meaning
    print(f"The word '{word}' has been successfully added to the dictionary.")

def main():
    while True:
        print("\nChoose the process to implement:")
        print("1. Find the meaning of a word")
        print("2. Add a new word")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue
        
        if choice == 1:
            word = input("Enter the word you want to search for its meaning: ")
            meaning = find_meaning(word)
            print(f"Meaning of the word '{word}': {meaning}")
        
        elif choice == 2:
            word = input("Enter the new word: ")
            meaning = input("Enter the meaning of the word: ")
            add_word(word, meaning)
        
        elif choice == 3:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()