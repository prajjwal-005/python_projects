import random  # for picking a random word
import hangman_words  # this is my file with the word list
from hangman_art import stages, logo  # this has all the ASCII art (the hangman stages and the title)

# --- Game Setup ---
lives = 6  # how many guesses the player gets
print(logo)  # print the main title screen

# Picking a random word from my word_list
difficulty = input("Choose a difficulty (easy, medium, hard, killer): ").lower()

# --- 3. CHOOSE THE WORD LIST ---
# Check the user's input and set the 'wordlist' variable
if difficulty == "medium":
    wordlist = hangman_words.medium_words
elif difficulty == "hard":
    wordlist = hangman_words.hard_words
elif difficulty == "killer":
    wordlist = hangman_words.killer_words
else:
    # If they type "easy" or any other nonsense, default to easy.
    if difficulty != "easy":
        print("Invalid choice. Defaulting to easy.")
    wordlist = hangman_words.easy_words
chosen_word = random.choice(wordlist)
word_length = len(chosen_word)  # need this to make the blanks



# Create the blank display list, e.g., ['_', '_', '_', '_']
# This is a  trick to make a list with n number of items
display = ["_"] * word_length

# This list will keep track of *all* guesses, right or wrong
guessed_letters = []

# This is my "flag" variable. The game loop will run as long as this is False.
game_over = False

# .join() turns my list ['_', '_', '_'] into a string "_ _ _" so it looks nice
print(f"Word to guess: {' '.join(display)}")

# --- Main Game Loop ---
# this 'while' loop is the main engine of the game
while not game_over:

    print(f"You have {lives} lives left.")
    guess = input("Guess a letter: ").lower()  # get the guess and make sure it's lowercase

    # Check if the player already tried this letter
    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'. Try again.")
        # 'continue' just skips the rest of this loop and goes back to the top
        continue

    # If it's a new guess, add it to our list of guessed letters
    guessed_letters.append(guess)

    # --- Check if the guess is correct ---
    found_letter = False

    # loop through the chosen word, one letter at a time
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter  # update the display list with the correct letter
            found_letter = True  # flip the flag to True, the guess was right!

    # --- Check if the guess is incorrect ---
    # if found_letter is still False, it means the guess was wrong
    if not found_letter:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1  # take away a life

        # Check if player is out of lives
        if lives == 0:
            game_over = True  # this will stop the while loop
            print("***********************YOU LOSE**********************")
            print(f"The correct word was: {chosen_word}")

    # --- Update Player ---

    # Show the current state of the word (with any new letters)
    print(f"Word to guess: {' '.join(display)}")

    # Check if the player has won
    # If there are no more "_" blanks in our display list, they must have won!
    if "_" not in display:
        game_over = True  # stop the loop
        print("****************************YOU WIN****************************")

    # Print the hangman art

    print(stages[lives])