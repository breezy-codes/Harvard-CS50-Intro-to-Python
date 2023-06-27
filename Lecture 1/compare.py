# Lecture 1
# Program task number 1
# program to test using conditionals

# Asks the users for the values of x and y
x = int(input("What's x? "))
y = int(input("What's y? "))

# Conditionals to check if x is less than y, greater than y or equal to y
# This method is not efficient as it checks all the conditions even if the first one is met.
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x ==y:
    print("x is equal to y")
    
# Proper method for conditional loops
# This method is more efficient than the previous one as it only needs to check for the first condition,
# if it is not met, it will check the next condition and so on.
if x < y:       # The first condition should be "if" as it is the first condition to check
    print("x is less than y")
elif x > y:     # All conditions between the first and last should be "elif" as they are the conditions to check
    print("x is greater than y")
else x == y:     # The final condition should be "else" as its the final condition to check
    print("x is equal to y")

# Using or conditionals to check if x is less than y or greater than y using an or conditional
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Alternatively it can be written as
if x != y: # != means not equal to
    print("x is not equal to y")
else:
    print("x is equal to y")