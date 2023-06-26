# Lecture 4
# Program task number 6
# Creating my own library to use in python

# This is the main module of the library created, and it stores all the functions
def main():
    hello("world")
    goodbye("world")

# This is the function that takes an input and displays hello "input"
def hello(name):
    print(f"Hello, {name}!")

# This is the function that takes an input and displays goodbye "input"
def goodbye(name):
    print(f"Goodbye, {name}!")
   
# This method of calling in main means it only calls in the function requested
# Without using this if line, when calling in a particular function from this library, it will instead call in all functions
if __name__ == "__main__": 
    main()