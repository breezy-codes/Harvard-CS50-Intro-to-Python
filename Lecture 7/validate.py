# Lecture 7
# Program task number 1
# Program to validate if an email address is correct

# Collect the users email address and strip any spaces from start or end
email = input("Enter your email address: ").strip()

# Checks if the email has an @ symbol and a dot in it and prints valid or invalid
#if "@" in email and "." in email:
#    print("Valid")
#else:
#    print("Invalid")
    
# A better way to do it is - 

# Split the email address into username and domain
username, domain = email.split("@")

# By using this method, we can check if the username by checking if it has any value
# You can use - "." in domain - to check if there is a dot in the domain part of the email
# Instead im using ".edu.au" to check if this email is a student email
if username and domain.endswith("edu.au"):
    print("Valid")
else:
    print("Invalid")
    
