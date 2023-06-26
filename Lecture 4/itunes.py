# Lecture 4
# Program task number 5
# A program to replicate itunes

import requests
import sys
import json

# Check for correct number of command line arguments, we only want the file name and the artist name
if len(sys.argv) != 2:
    sys.exit( )

# Get the response from the itunes API and the users input of the artist name limited to one result
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# Print out the response as a json object and formatted with an indent of 2
print(json.dumps(response.json(), indent=2))

# A way to print out only the information wanted
o = response.json()
for result in o["results"]:
    print(result["trackName"])