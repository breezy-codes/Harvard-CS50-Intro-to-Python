# Lecture 1
# Program task number 3
# Check if a number is even or odd

# Ask the user for a number
x = int(input("What's x? "))

# Checks is the number has a remainder of 0, if it does the number is even
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")


#Version 2
# Alternatively you can create a function to use this in multiple instances in a program
# This is the main function, it asks the user for a number and then calls the is_even function
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

# Function to check if a number is even using the same as before, but now as a function.
# This function uses a bool to return true or false on whether the number is even or not.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
# Alternatively you can use the following code to do the same thing with less lines
def is_even(n):
    return True if n % 2 == 0 else False

# You can also simplify this further by removing the if statement
def is_even(n):
    return n % 2 == 0

#then calls the main function
main()