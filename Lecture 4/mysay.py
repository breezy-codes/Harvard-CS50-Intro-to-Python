# Lecture 4
# Program task number 7
# Using funny libraries

# This is the way to import a specific function from a library
from sayings import hello
import sys

# Checking the number of arguments the user has entered
# If they have entered the program name, and the name of the person they want to say hello to, then it will run the hello function
if len(sys.argv) == 2:
    hello(sys.argv[1])