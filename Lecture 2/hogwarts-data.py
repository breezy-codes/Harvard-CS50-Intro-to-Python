# Lecture 2
# Program task number 4
# Creating a list of dictionaries

# the list of students as a list of dictionaries
# Each line is its own dictionary that contains the name, house, and patronus of the student
students = [
    {"Name": "Hermione", "House": "Gryffindor", "patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "patronus": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"Name": "Draco", "House": "Slytherin", "patronus": None}
]

# printing out the list of students with their houses from the list of dictionaries
for student in students:
    print(student["Name"], student["House"], sep=": ")
    print(student["patronus"])
    print()