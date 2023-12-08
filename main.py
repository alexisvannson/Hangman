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


# generate one underscore for each letter in the genrerated word
seen_word = ["_"]*len(random_english_word)
false_guesses = []
#store already seen letter
seen_letter = []
#store correct letters :
correct =[]
# initialize turtle
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)


# draw gallows
turtle.home()
turtle.pendown()
turtle.left(90)
turtle.forward(175)
turtle.left(90)
turtle.forward(74)
turtle.left(90)
turtle.forward(35)
turtle.penup()
turtle.goto(-135,-35)


# draw the hangman 
def drawMan(x):
    guess = x
    if guess == 1: 
        # draw head
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15,None,100)
        turtle.penup()
    elif guess == 2:
        # draw torso
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
    elif guess == 3:
        # draw first arm
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif guess == 4:
        # draw second arm
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif guess == 5:
        # draw first leg
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
    elif guess == 6:
        # draw second leg
        turtle.goto(-74, 70)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()

display_word()
