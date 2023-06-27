# Lecture 5
# Program task number 1
# A calculator program, to calculate the square of a number

# This program will ask the user for a number, and then square it
def main():
    x = int(input("What's x?: "))
    print("x squared is", square(x))
 
# This function will square the number that the user entered   
def square(n):
    return n * n

# Using this if statement, the program will only run if a specific condition is met
if __name__ == "__main__":
    main()