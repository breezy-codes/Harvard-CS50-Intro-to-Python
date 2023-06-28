# Lecture 8
# Program task number 2
# Object oriented program for the harry potter houses

# Define the Student class
# This is the blueprint for the student object and contains the name and house
# It also includes error checking to make sure the name and house are valid
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Name is required")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("House is not valid")
        self.name = name
        self.house = house
        self.patronus = patronus

# Define the __str__ function to return the name and house
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    def charm(self):
        print(f"{self.name} is casting a charm")

# Define the main function to call the other functions
# This is the function that will be called when the program is run
def main():
    # Call the get_student function and store the returned values in the student variable
    student = get_student()
    print(f"{student.name} is from {student.house}")


# Define the get_student function to collect the users name and house in one function
# This could of been done as two functions get_name and get_house,
# but you can actually return multiple values from a single function
def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return Student(name, house)

# Call the main function to run the program using the if statement to check if the program is being run directly
if __name__ == "__main__":
    main()
