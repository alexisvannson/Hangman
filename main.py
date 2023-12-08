# import a list of 236736 english words with the nltk module
import nltk
import turtle 
import random

nltk.download('words')
from nltk.corpus import words

# assign the list to the word_list variable
word_list = words.words() 

#import the random module to generate a random index to retrieve a random word of the imported wordlist
random_english_word_not_formated = word_list[random.randint(1,len(word_list))]
random_english_word = random_english_word_not_formated.upper()

# Function to display guessed letters
def display_guessed_letters():
    turtle.goto(-200, -100)  # Set the position where you want to display the guessed letters
    turtle.write("Guessed Letters: " + " ".join(seen_letter), font=("Courier", 14, "normal"))


# Initialize the display for the word
def display_word():
    turtle.goto(-135, -35)  # Adjust the position as needed
    turtle.write(' '.join(seen_word), font=("Courier", 14, "normal"))

# Update the displayed word
def update_display(new_guess):
    for idx, letter in enumerate(random_english_word):
        if letter == new_guess:
            seen_word[idx] = new_guess



# in the hangman game you loose on the 7th mistake, while we are alive we can guess a letter
# The function `display_word` is called to display the initial state of the word (probably with underscores).
display_word()

# The game continues as long as the number of false guesses is less than or equal to 6.
while len(false_guesses) <= 6:
    # Asking the player for a new guess using Turtle's text input dialog.
    new_guess_not_formated = str(turtle.textinput('Hangman', 'Guess a letter:'))
    # Converting the guess to uppercase.
    new_guess = new_guess_not_formated.upper()

    # If the guess is not the complete word and is more than one letter, it skips the rest of the loop.
    if new_guess != random_english_word and len(new_guess) > 1:
        continue 

    # Check if the guessed letter is in the word.
    if new_guess in random_english_word:
        # Add the correct guess to the list of seen letters.
        seen_letter.append(new_guess)
        # Update the display to show the correctly guessed letter.
        update_display(new_guess)
        # Display all guessed letters.
        display_guessed_letters()

        # Check if the word is completely guessed or if the guess is the entire word.
        if "_" not in seen_word or new_guess == random_english_word:
            # Display "You Win!" using Turtle Graphics.
            turtle.goto(0, 225)
            turtle.color('green')
            turtle.write("You Win!", align="center", font=("Courier", 55, "bold"))
            # Also display the correct word.
            turtle.goto(0, 200)
            turtle.write("The Word Was: " + random_english_word, align="center", font=("Courier", 14, "bold"))
            # Hide the turtle and end the Turtle Graphics session.
            turtle.hideturtle()
            turtle.done()
            break
    
