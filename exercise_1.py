# Use lists, dictionaries, strings, and variables
# List with names of our friends: Mary, John, and Alex
# Dictionary: key
# Names: keys
# Values: # of characters in name
# Refer to dictionary and list as variable
# Print off all name's lengths
# No hard-coding in keys and values!
# Ex. Searching or Mary using friends['Mary']
# Optional: add in more names

friends = ["Mary", "John", "Alex"]
people = {"Mary": 4, "John": 4, "Alex": 4}

print(people[friends[0]])
print(people[friends[1]])
print(people[friends[2]])

people["Jeremy"] = 6

for name in friends:
    print(people[name])