import random
from words import words  # Ensure you have a words.py file with a list of words
import string

def get_valid_word(words):
    word = random.choice(words).upper()  # Convert word to uppercase for consistency
    while '-' in word or ' ' in word:  # Ensure no spaces or hyphens
        word = random.choice(words).upper()
    return word

def hangman():
    word = get_valid_word(words)  # Get a random word
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)  # A-Z letters
    used_letters = set()  # Letters guessed by the user
    lives = 6  # Maximum wrong guesses allowed

    print("Welcome to Hangman! You have 6 lives.")

    while len(word_letters) > 0 and lives > 0:  # Continue until word is guessed or lives run out

        # Show used letters
        print("\nYou have", lives, "lives left and you have used these letters:", " ".join(sorted(used_letters)))

        # Display current word (guessed letters + hidden dashes)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word:", " ".join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        # Check if input is valid
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Correct guess
            else:
                lives -= 1  # Incorrect guess
                print("Wrong guess! The letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")

        else:
            print("Invalid input. Please enter a letter.")

    # Game over messages
    if lives == 0:
        print("\n💀 You lost! The word was:", word, "💀")
    else:
        print("\n🎉 Congratulations! You guessed the word:", word, "🎉")

# Ensure the game runs only when executed directly
if __name__ == "__main__":
    hangman()
