# Lecture 6
# Program task number 1
# A list

# A list of names
names=[]

# Prompt user for names
for _ in range(3):
    names.append(input("Whats your name? "))
 
for name in sorted(names):
    print(f"Hello, {name}!")