# Lecture 6
# Program task number 1
# A program that collects a list of names

# A list of names
names=[]

# Prompt user for names
for _ in range(3):
    names.append(input("Whats your name? "))

# Print the names in order alphabetically
for name in sorted(names):
    print(f"Hello, {name}!")