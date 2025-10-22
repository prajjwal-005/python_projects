Hangman Game 🐍
===============

This is a classic command-line Hangman game built in Python. It was my first project while learning the fundamentals of Python programming.

Description
-----------

The game picks a secret word, and the player must guess it, one letter at a time. The player has 6 "lives," and each incorrect guess brings them one step closer to losing. The goal is to guess the word before running out of lives!

Features
--------

*   **Random Word Selection**: The game picks a random word from a large list.
    
*   **Lives System**: You start with 6 lives, which decrease with every wrong guess.
    
*   **ASCII Art**: Displays the Hangman stages and a logo, which update as you lose lives.
    
*   **Progress Tracking**: Shows your progress with underscores for unguessed letters (e.g., \_ p p \_ e).
    
*   **Duplicate Guess Handling**: Remembers all letters you've guessed (both right and wrong) and lets you know if you've already tried a letter.
    
*   **Win/Loss Conditions**: The game clearly tells you if you've won or lost, revealing the secret word if you lose.
    

How to Run the Project
----------------------

### Prerequisites

*   You must have **Python 3** installed on your computer.
    

### Required Files

Make sure all these files are in the **same folder**:

*   hangman.py (The main game code)
    
*   hangman\_words.py (Contains the word\_list)
    
*   hangman\_art.py (Contains the stages and logo ASCII art)
    

### Running the Game

1.  Open your terminal or command prompt.
    
2.  cd path/to/your/hangman-project
    
3.  python hangman.py
    

How to Play
-----------

1.  Run the game as shown above.
    
2.  You will see the Hangman logo and a set of blank spaces for the secret word.
    
3.  Enter a single letter as your guess and press Enter.
    
4.  If the letter is correct, it will appear in its correct position(s).
    
5.  If the letter is wrong, you will lose a life, and the Hangman drawing will update.
    
6.  Keep guessing letters until you either guess the entire word (You win!) or you run out of lives (You lose!).
    

What I Learned from This Project
--------------------------------

This project was a fantastic way to apply beginner Python concepts. I learned how to:

*   Import modules (random) and variables from my own files (hangman\_words, hangman\_art).
    
*   Use while loops to create the main game loop.
    
*   Use for loops to iterate over a string or list (like checking the chosen\_word).
    
*   Work with **Lists** (especially for the display and guessed\_letters).
    
*   Use **String Methods** like .lower() to handle user input and .join() to display the board.
    
*   Manage game state with **Boolean Flags** (game\_over, found\_letter).
    
*   Use if/else conditional logic to check guesses, lives, and win/loss conditions.

### here are some screenshot of how it will look

<img width="1861" height="926" alt="Screenshot (33)" src="https://github.com/user-attachments/assets/cb9deebb-601a-45ae-af70-ec6a16ab22d8" />
<img width="1920" height="918" alt="Screenshot (34)" src="https://github.com/user-attachments/assets/4c26e95a-5857-4f3c-abb8-4d9a0d13c0b8" />
<img width="1920" height="944" alt="Screenshot (35)" src="https://github.com/user-attachments/assets/0251f083-46f9-4d70-99d5-f30cbadc7326" />
<img width="1920" height="891" alt="Screenshot (36)" src="https://github.com/user-attachments/assets/e40bd5c7-4163-4854-99e1-62dfdf4918d5" />
<img width="1920" height="924" alt="Screenshot (37)" src="https://github.com/user-attachments/assets/0b8a4723-3cb1-4e90-ac45-362e3eb5fcd6" />
<img width="1920" height="890" alt="Screenshot (39)" src="https://github.com/user-attachments/assets/4e6b12dc-8990-41bc-be2d-cc78648cb0c4" />
