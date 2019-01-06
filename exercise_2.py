friends = ["Mary", "John", "Alex"]
people = {"Mary": 4, "John": 4, "Alex": 4, "Jeremy": 6}

print(people.keys())
print(people.values())
print(people.items())

for k in people.keys():
    print(k)

for k, v in people.items():
    print(k, v)

for k, v in people.items():
    if k in friends:
        print(v)