# Lecture 7
# Program task number 2
# Program to validate if an email address is correct using import re

import re

# Collect the users email address and strip any spaces from start or end
email = input("Enter your email address: ").strip()

# Use the re function to check the email address for specific characters and symbols to check if its valid
if re.search(r".+@.+.\.edu", email):
    print("Valid")
else:
    print("Invalid")
    
