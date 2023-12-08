# Hangman Game


## Overview
Welcome to the Hangman game! This simple Python-based Hangman game challenges you to guess a word letter by letter. Your goal is to guess the entire word before the hangman is fully drawn. The game features an interactive interface, gallows drawing, and helpful feedback.

## How to Play
1. **Run the Python script:** Ensure you have Python 3.x installed. If not, download it from [python.org](https://www.python.org/downloads/). Additionally, install the NLTK library by running `pip install nltk` in your terminal.

2. **Launch the game:** Run the Hangman game script.

3. **Initial Display:** The game will display underscores representing each letter in the word.

4. **Guess a Letter:** Enter a letter in the input box to make a guess.

5. **Feedback:** If the guessed letter is in the word, it will be revealed in its correct position. Otherwise, the hangman drawing will progress.

6. **Continue Guessing:** Keep guessing until you either correctly guess the entire word or the hangman is fully drawn.

## Game Features
- **Gallows Drawing:** The hangman is dynamically displayed as you make incorrect guesses. The interface is generated using the Turtle graphics library.
  
- **Guessed Letters:** Track your progress with a display of guessed letters and their positions in the word.

- **Winning and Losing:** The game concludes with a celebratory message if you successfully guess the word. Conversely, if you make too many incorrect guesses, a defeat message is displayed.
Certainly! Here's an explanatory section that breaks down the logic behind the Hangman game code:

## Breakdown of the underlying logic 

### Word Selection and Initialization

1. **Importing Words:**
   - The game starts by importing a list of 236,736 English words using the NLTK module.

2. **Choosing a Random Word:**
   - A random word is selected from the word list using the `random.randint` function.

3. **Formatting and Initialization:**
   - The selected word is converted to uppercase to standardize input.
   - The initial state of the game is set up, including the display for guessed letters, correct guesses, and the word itself.

### Drawing the Gallows and Hangman

4. **Drawing the Gallows:**
   - The Turtle graphics module is used to draw the initial gallows.

5. **Drawing the Hangman:**
   - The `drawMan` function defines the logic to draw different parts of the hangman based on the number of incorrect guesses.

### User Input and Guessing

6. **Getting User Input:**
   - The game prompts the user to guess a letter using the `turtle.textinput` function.

7. **Validating User Input:**
   - The code checks if the input is a single letter and not the entire word. If not, it skips the current iteration.

8. **Checking Guessed Letter:**
   - If the guessed letter is in the word, it is added to the list of seen letters, and the displayed word is updated accordingly.

### Win and Lose Conditions

9. **Checking Win Condition:**
   - The game checks if all letters in the word are guessed correctly. If so, it displays a "You Win!" message.

10. **Checking Lose Condition:**
   - If the maximum number of incorrect guesses (6) is reached, it displays a "You LOOSE!" message along with the correct word.

### Displaying Information

11. **Displaying Guessed Letters:**
   - The `display_guessed_letters` function updates and displays the list of guessed letters.

12. **Displaying the Word:**
   - The `display_word` and `update_display` functions handle displaying the word with underscores and updating it with correct guesses.

### Ending the Game

13. **Ending the Game:**
   - The game ends when the user either correctly guesses the word or reaches the maximum allowed incorrect guesses.

14. **Final Output:**
   - The final outcome (win or lose) is displayed using Turtle graphics.

---

This logic breakdown outlines the key steps and functions that contribute to the functionality of the Hangman game.
## Requirements
- Python 3.x
- NLTK library (Natural Language Toolkit)

## Installation
1. **Install Python:** Download and install Python 3.x from [python.org](https://www.python.org/downloads/).

2. **Install NLTK:** Open your terminal or command prompt and run `pip install nltk`.

3. **Run the Hangman Game:** Execute the Hangman game script.

Enjoy the challenge of Hangman and have fun guessing the words!

