# Lecture 4
# Program task number 3
# A program to use a library called

# Import the library called sys
import sys

# Check if the number of arguments is correct using error testing
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
# The sys.argv[1] is the first argument after the program name
# The sys.argv[0] is the program name
# In terminal when running you run "python l4-name.py name" where name is the argument
else :
    print("Hello, my name is", sys.argv[1])
    
# A better way to check the number of arguments as it exits the program when conditions aren't met
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    
    
# A way to check for all names in the argument using only a check for not enough arguments
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# For loop to print all names in the argument
# However this way also prints out the first name as name.py
for arg in sys.argv:
    print("Hello, my name is", arg)

# How to slice the list to only print the names
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)