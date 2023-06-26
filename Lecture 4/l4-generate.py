# Lecture 4
# Program task number 1
# A program to use a library called random

#Method one, to import the entire library - 
#
# This method imports the entire library random and allows you to use any function from the library
import random

#Then use the module to call the function you want to use
coin = random.choice(["Heads", "Tails"])
print(coin)

#Method two, to import a specific function from the library - random
#
# This method instead imports the exact function you want to use from the library random
from random import choice 

#Then use the function directly without referring to the library
coin = choice(["Heads", "Tails"])
print(coin)

# This function "randint" can be used to generate a random integer between two numbers
number = random.randint(1, 10)
print(number)

# This function "shuffle" can be used to shuffle a list
# Create a list of cards
cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
# A function using the import random to shuffle the list of cards
random.shuffle(cards)
#the for loop allows the cards to be printed out in a list
for card in cards:
    print(card)