# Lecture 6
# Program task number 2
# A list of names saved to a txt file

name = input("What's your name? ")

# Open the file for appending, a is for appending, w is for writing
# w will just change the entire file, but a just adds to the end of the file
with open("names.txt", "a") as file:  
    #Format the name and write it to the file
    file.write(f"{name}\n")
    
# Open the file for reading using the command r
with open("names.txt", "r") as file:
    lines = file.readlines()