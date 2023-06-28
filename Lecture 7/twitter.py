# Lecture 7
# Program task number 4
# Program to extract the twitter username

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"username: {username}")