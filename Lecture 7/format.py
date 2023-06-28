# Lecture 7
# Program task number 3
# Program to format data

import re

# Collects the users name and strips any spaces from start or end
name = input("What's your name? ").strip()
# Checks if the name is in the format of "last, first" and if so, splits the name into two variables
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"Hello {name}!")

# Instead it can be done using re search
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
    
print(f"Hello {name}!")