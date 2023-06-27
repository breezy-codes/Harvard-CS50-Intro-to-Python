# Lecture 6
# Program task number 5
# Shows a list of names from a csv file

family = []

# Open the file and read each row from the CSV file
with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        # This will print out the two columns in the CSV file for each row
        print(f"{row[0]} is a {row[1]}")



# Method two defines what each column in the csv file is
with open("names.csv") as file:
    for line in file:
        name, species = line.rstrip().split(",")
        # This will print out the two columns in the CSV file for each row
        family.append(f"{name} is a {species}")
        
# It then prints them sorted alphabetically
for family in sorted(family):
    print(family)

#Method 3 using dictionaries, its more code but it defines the columns and stores them in a dictionary
with open("names.csv") as file:
    for line in file:
        name, species = line.rstrip().split(",")
        family = {"name": name, "species": species}
        family.append(family)
        
# It then prints them sorted alphabetically
for family in sorted(family):
    print(f"{family['name']} is a {family['species']}")