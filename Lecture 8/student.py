# Lecture 8
# Program task number 1
# Object oriented program for the harry potter houses


# Define the main function to call the other functions
# This is the function that will be called when the program is run
def main():
    # Call the get_student function and store the returned values in the student variable
    student = get_student()
    print(f"{student['name']} is from {student['house']}")


# Define the get_student function to collect the users name and house in one function
# This could of been done as two functions get_name and get_house,
# but you can actually return multiple values from a single function
def get_student():
    student = {}
    student["name"] = input("Enter your name: ")
    student["house"] = input("Enter your house: ")
    return student


# Call the main function to run the program using the if statement to check if the program is being run directly
if __name__ == "__main__":
    main()
