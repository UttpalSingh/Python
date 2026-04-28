print("mutable and immurable")

username = "Virat"
print(username)
username = "kohli "
print(username)

# username is string and string is immutable.
# Here we pass the reference of username to kohli from Virat but actually there is no change in username.
# because of automatic garbage collection in python Virat will be deleted from the memory automatically and new value of username will be kohli.