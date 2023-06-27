# Lecture 6
# Program task number 3
# A program that displays the list of the names created in the names.py program


# Open the file for reading using the command r
with open("names.txt", "r") as file:
    lines = file.readlines()

# Print out all the names that were given to the .txt file
for line in lines:
    print("Hello,", line.rstrip())
    
    
# Alternatively you can simplify this into being just:
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
