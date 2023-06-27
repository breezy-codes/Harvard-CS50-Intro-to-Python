# Lecture 6
# Program task number 6
# Shows a list of names from a csv file

import csv

students = []

# Open the file and read each row from the CSV file
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})
# It then prints them sorted alphabetically       
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# Secondary method using a dict reader from the csv module
# This method instead infers from the first row of the csv what the columns are
# Then it uses the column names as keys for the dictionary
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# It then prints them sorted alphabetically       
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")