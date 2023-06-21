# Lecture 3
# Program task number 1
# A program to test error exceptions

# Using try and except to catch errors
try:                   # Using try to collect an integer from the user
    x = int(input("Whats x? "))
    print(f"X is {x}")
except ValueError:     # If the user enters a non-integer
    print("X is not an integer")


# Introducing a while loop to get the input correctly while using try and except to catch errors
while True:
    try:                   # Using try to collect an integer from the user
        x = int(input("Whats x? "))
    except ValueError:     # If the user enters a non-integer
        print("X is not an integer")
    else:
        break
print(f"X is {x}")

# Create a main function to be called
def main():
    x = get_int()
    print(f"X is {x}")

# Create a function to get an integer from the user and check if it is an integer
def get_int():
    while True:
        try:                   # Using try to collect an integer from the user
            x = int(input("Whats x? "))
        except ValueError:     # If the user enters a non-integer
            print("X is not an integer")
        else:
           return x

main()

#Alternative way to do the same thing with less lines of code as - 
# Create a function to get an integer from the user and check if it is an integer
def get_int():
    while True:
        try:                   # Using try to collect an integer from the user
             return int(input("Whats x? "))
        except ValueError:     # If the user enters a non-integer
            print("X is not an integer")