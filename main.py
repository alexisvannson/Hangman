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
    display_word()



