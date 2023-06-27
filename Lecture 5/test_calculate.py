# Lecture 5
# Program task number 2
# A program to specifically test the calculator program

# Import the square function from calculate.py file 
from calculate import square

def main():
    test_square()

# This function will test the square function
# This method is not ideal, as it only tests the square function by checking if the value isn't 4 or 9
def test_square():
    if square(2) != 4:
        print("Test failed, 2 squared wasn't 4")
    if square(3) != 9:
        print("Test failed, 3 squared wasn't 9")
    
# This is a better method for checking if the test passed or failed
# This method checks if the value is equal to the expected value, else prints the problem
# This method strictly tests the built in square function
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("Test failed, 2 squared wasn't 4")
    try:
        assert square(3) == 9    
    except AssertionError:
        print("Test failed, 3 squared wasn't 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("Test failed, -2 squared wasn't 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("Test failed, -3 squared wasn't 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("Test failed, 0 squared wasn't 0")

# Using this if statement, the program will only run if a specific condition is met
if __name__ == "__main__":
    main()
    
    