# Lecture 2
# Program task number 1
# This program meows like a cat

# Starter code
# Prints meow out 3 times
print("Meow!")
print("Meow!")
print("Meow!")


############################################################################################################



# using while loops
# Using a loop to print meow out 3 times
i = 3  # i is a variable that keeps track of how many times we have printed meow, initialised to 3
while i != 0:      # While i is not equal to 0, keep printing meow
    print("Meow!")
    i = i - 1      # Without this line, the loop will run forever, as i will never be equal to 0

# Another method of using a loop but allowing for different number of meows from the while loop
i = 0  # i is initialised as 0 to allow for the while loop to run with different variable values
while i < 3:      # While i is less than 3, keep printing meow
    print("Meow!")
    i += 1      # This syntax increments i by 1, same as i = i + 1


############################################################################################################


# Using for loops
# Using a for loop to print meow out 3 times
# This version uses a list you need to write out for each number to run through
for i in [0, 1, 2]:  # in python you should use _ instead of i if you don't need to use the variable
    print("Meow!")

# This version uses a range, in the case set to 3
# range(3) is the same as [0, 1, 2] but simplified for any amount of times
for _ in range(3):  # _ is the same as using i, but it is a convention to use _ if you don't need to use the variable
    print("Meow!")


############################################################################################################



# This is another method for printing the same text multiple times by using multiplication
print("Meow!" * 3)  # however it prints like "Meow!Meow!Meow!"

# \n is a special character that means new line, so it prints with Meow! on a new line each time
print("Meow!\n" * 3) # However this ends on an empty line when you run it

# This is a way to remove the empty line at the end of the print statement
print("Meow!\n" * 3, end="")  # This is a way to remove the empty line at the end of the print statement


############################################################################################################



# Implementing a way for the user to select how many meows they want
while True:
    n = int(input("How many meows do you want? "))
    if n > 0: #This loop runs until you reach 0
        break

# This is a way to print meow n times
for _ in range(n):
    print("Meow!")


############################################################################################################



# This is a way to print meow n times using functions
# Create a function for meow, this is a method for using meow in a program as a function
def main():
    number = get_number()
    meow(number)

# This is a function that gets the number of meows the user wants
def get_number():
    while True:
        n = int(input("How many meows do you want? "))
        if n > 0: # this if function will return the value, only if its above 0
            return n
    
def meow(n):
    for _ in range(n):
        print("Meow!")
        
main()