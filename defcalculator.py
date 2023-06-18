# Program Task Number 5
# This program is for a simple calculator that now also includes a function

def main():
    x = int(input("What's x? "))
    print("X squared is", square(x))
    
def square(n):
    return n * n # You can also do n ** 2 which raises n to the power of 2

main()