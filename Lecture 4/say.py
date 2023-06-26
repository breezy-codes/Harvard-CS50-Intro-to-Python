# Lecture 4
# Program task number 4
# Using funny libraries

import cowsay
import sys

# Checks the user input for the program name, and an entered name
# If the user enters only the program name and their name, it will print the default message
# This will print with a cow saying hello name
if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    
# Checks the user input for the program name, and an entered name
# If the user enters only the program name and their name, it will print the default message
# This will print with a trex saying hello name
if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])
    
# Checks the user input for the program name, and an entered name
# If the user enters only the program name and their name, it will print the default message
# This will print with a pig saying hello name
if len(sys.argv) == 2:
    cowsay.pig("Hello, " + sys.argv[1])