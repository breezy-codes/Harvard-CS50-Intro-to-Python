# Lecture 2
# Program task number 5
# Simulating the blocks in a mario game and positioning them in a column

# Creating the main to print 3 vertical # blocks
def main():
    print_column(3)
    
# Creating the print_column function to print the # blocks
def print_column(height):
        print("#\n" * height, end="")
        
main()