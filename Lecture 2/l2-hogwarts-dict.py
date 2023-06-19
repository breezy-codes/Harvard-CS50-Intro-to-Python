# Lecture 2
# Program task number 3
# Program for using lists and printing them out in different ways, using dictionaries

# the variable list of students as a dictionary
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# printing out the list of students with their houses from the dictionary
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# printing out the list of students with their houses from the dictionary using a for loop
# This is a simpler way to print out a list of students with their houses
for student in students:
    print(student, students[student], sep=": ")
