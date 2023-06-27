# Lecture 1
# Program task number 2
# program to calculate the students grade

# Asks the user for the score of their grade
score = int(input("Score: "))

# Conditionals to check the grade based on the given score
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# Alternatively it can be written as
# This method is more simpler and easier to understand than the above one
# It removes the need to write score twice and the "and" operator
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# Another method can be used if we know the maximum score is 100
# This method is more simpler and easier to understand than the above one
# In this method it checks the score and works down, so if the score is 90 or above it will print A and not check the other conditions
# Because of the logic, if the score is less than 90, it then checks the next range down, which is 80, and so on
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
