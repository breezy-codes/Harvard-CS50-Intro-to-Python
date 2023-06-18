# Program task number 2
# Program to ask the user for their name and greet them
# This covers different ways to display the name
# This also goes over formatting for the name, as well as splitting up the inputs

# Version 1
print("Version 1 - Starter Code")
# Take the user input for their name
name = input("What's your name? ")
# print out Hello + The user's name input
print("Hello, " + name)

# Version 2
print("Version 2 - Uses Comma")
# Take the user input for their name
name = input("What's your name? ")
# This version uses the print statement with a comma to output multiple strings
print("Hello,", name, name)

# Version 3
print("Version 3 - Uses End")
# Take the user input for their name
name = input("What's your name? ")
# This version uses the end="" to remove the new line that is automatically added to the end of the print statement
print("Hello, ", end="")
print(name)

# Version 4
print("Version 4 - Uses Sep")
# Take the user input for their name
name = input("What's your name? ")
# This version uses the sep="" to remove the space that is automatically added between the strings
print("Hello,", name, sep='')

# Version 5
print("Version 5 - Uses F-String")
# Take the user input for their name
name = input("What's your name? ")
# This version uses the f-string to format the string, the modern way to do it
print(f"Hello, {name}")

# Version 6
print("Version 6 - Uses formatters")
# Take the user input for their name
name = input("What's your name? ")
# Removes whitespace from the start and end of the string
name = name.strip()
# Capitalizes the first letter of the string
name = name.capitalize()
# Capitalizes the first letter of each word in the string
name = name.title()
# This version uses the f-string to format the string, the modern way to do it
print(f"Hello, {name}")

# Version 7
print("Version 7 - Groups formatters")
# Take the user input for their name
name = input("What's your name? ")
# Removes whitespace from the start and end of the string, then capitalizes the first letter of each word in the string
# This groups these functions into one line
name = name.strip().title()
# This version uses the f-string to format the string, the modern way to do it
print(f"Hello, {name}")

# Version 8
print("Version 8 - Groups formatters to one line")
# Take the user input for their name, and includes the formatting all into one line
name = input("What's your name? ").strip().title()
# This version uses the f-string to format the string, the modern way to do it
print(f"Hello, {name}")

# Version 9
print("Version 9 - Groups formatters to one line and splits words")
# Take the user input for their full name, and includes the formatting all into one line
name = input("What's your full name? ").strip().title()
# Split the users name ino first name and last name
first, last = name.split(" ")
# This version uses the f-string to format the string, the modern way to do it
print(f"Hello, {first}")
