# Lecture 2
# Program task number 2
# Program for using lists and printing them out in different ways

# the variable list of students
students = ["Hermione", "Harry", "Ron"]

# prints the list of students by printing each element in the list
print(students[0])  # prints Hermione
print(students[1])  # prints Harry
print(students[2])  # prints Ron

# prints the list of students by using a for loop to list all students
for student in students:
    print(student)  # prints Hermione, Harry, Ron
  
# This method uses len() to get the length of the list and then uses a for loop to print each element  
for i in range(len(students)):
    print(students[i])  # prints Hermione, Harry, Ron
    
# This method uses len() to get the length of the list and then uses a for loop to print each element with the index
for i in range(len(students)):
    print(i + 1, students[i]) # The i + 1 is to make the index start at 1 instead of 0, prints 1 Hermione, 2 Harry, 3 Ron