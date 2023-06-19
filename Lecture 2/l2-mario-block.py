# Lecture 2
# Program task number 7
# Prints a set of boxes similar to in the mario game

# Creating the main to print 3 square # blocks
def main():
    print_square(3)
    
# Creating the print_square function to print the # blocks
def print_square(size):
    #For each row in square
     for i in range(size):
         print("#" * size)
        
main()