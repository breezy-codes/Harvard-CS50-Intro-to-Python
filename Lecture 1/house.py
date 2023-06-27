# Lecture 1
# Program task number 4
# Ask the user for their name and add them into a HP house

# Ask the user for their name and store it in a variable name
name = input("What's your name? ")

# Checking if the name is in the list of names and then printing the house
if name == "Harry":
    print("You're in Gryffindor")
elif name == "Hermione":
    print("You're in Gryffindor")
elif name == "Ron":
    print("You're in Gryffindor")
elif name == "Draco":
    print("You're in Slytherin")
else:
    print("Who?")

# Version 2
# This method combines the names that are in the same house into one line of code to reduce the amount of code
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("You're in Gryffindor")
elif name == "Draco":
    print("You're in Slytherin")
else:
    print("Who?")

# Version 3
# Another method can be done using the "match" function in python
match name:
    case "Harry":       # These are the cases they will check to see if the name is in the list
        print("You're in Gryffindor")
    case "Hermione":
        print("You're in Gryffindor")
    case "Ron":
        print("You're in Gryffindor")
    case "Draco":
        print("You're in Slytherin")
    case _:         # This is the default case that will be used if none of the above cases are true
        print("Who?")

# Version 4
# This method simplifies down the match function by combining the names that are in the same house
match name:
    case "Harry" | "Hermione" | "Ron":      # These are the cases they will check to see if the name is in the list
        print("You're in Gryffindor")
    case "Draco":
        print("You're in Slytherin")
    case _:                                 # This is the default case that will be used if none of the above cases are true
        print("Who?")
