# Lecture 6
# Program task number 4
# A list of names saved to a txt file that is sorted alphabetically

names = []

# Open the file and read each line into a list
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

# Sort the list and then print out the names        
for name in sorted(names):
    print(f"Hello, {name}")

# By default sorted sorts in ascending order, to sort in descending order you can use reverse=True  
for name in sorted(names, reverse=True):
    print(f"Hello, {name}")