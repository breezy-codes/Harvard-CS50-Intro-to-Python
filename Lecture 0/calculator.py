# Lecture 0
# Program Task Number 3
# This program is for a simple calculator

# Version 1
print("Version 1 - Starter Code")
# Ask the user for two numbers
x = input("What's x? ")
y = input("What's y? ")
# Convert x and y to integers and calculates the sum
z = int(x) + int(y)
# Print the sum
print("The sum of x and y is:", z)

# Version 2
print("Version 2 - Uses Integers")
# Ask the user for two numbers and declare them as integers
x = int(input("What's x? "))
y = int(input("What's y? "))
# Calculate the sum
print("Print the sum of x and y", x+y)

# Version 3
print("Version 3 - Uses Floats")
# Ask the user for two numbers and declare them as floats to allow decimal points
x = float(input("What's x? "))
y = float(input("What's y? "))
# Calculate the sum
print("Print the sum of x and y", x+y)

# Version 4
print("Version 4 - Rounds the number")
# Ask the user for two numbers and declare them as floats to allow decimal points
x = float(input("What's x? "))
y = float(input("What's y? "))
# rounds the sum of x and y to 2 decimal places
z = round(x+y, 2)
# Calculate the sum
print("Print the sum of x and y", z)

# Version 5
print("Version 5 - Formats a large number with commas")
# Ask the user for two numbers and declare them as floats to allow decimal points
x = float(input("What's x? "))
y = float(input("What's y? "))
# rounds the sum of x and y to 2 decimal places
z = round(x+y, 2)
# Calculate the sum, and format it with commas
print("Print the sum of x and y", f"{z:,}")

# Version 6
print("Version 6 - Division")
# Ask the user for two numbers and declare them as floats to allow decimal points
x = float(input("What's x? "))
y = float(input("What's y? "))
# Calculate the division of x and y and round it to 2 decimal places
z = round(x / y, 2)
# Print the value of z
print("Print x divided by y", z)

# Version 7
print("Version 7 - Division done using f-string")
# Ask the user for two numbers and declare them as floats to allow decimal points
x = float(input("What's x? "))
y = float(input("What's y? "))
# Calculate the division of x and y
z = x / y
# Print the value of z to 2 decimal points
print("Print x divided by y", f"{z:.2f}")
