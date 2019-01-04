# comment

# data types
# numbers
# strings
# list
# tuple
# dictionary

print("hello world")

print(int(10.0))
print(float(10))
print(str(10))


hello = "hello world"
print(hello[0])
print(hello[0:4])
print(hello[-1])
print(hello[1:-1])
print(hello[-3:-1])

print("he" in "hello")
print("w" in "hello")

# lists
lister = [1,2,4, 'hello']
print(lister)
lister.append(2)
print(lister)
print(lister[0])
print(lister.index(1))
print(lister.index('hello'))
print(lister.count(2))
lister.remove(2)
print(lister)
lister.reverse()
print(lister)

numberList = [1, 5, 10, 6, 4, 7]
print(numberList)
numberList.sort()
print(numberList)

# dictionaries
tels = {"Mary": 4165, "John": 4512, "Jerry": 5555}
print(tels)
tels['Jane'] = 5432
print(tels)
print(tels['John'])
del tels['Jerry']
print(tels)

# tuples
tup = ("math", "football", 2020)
print(tup)
print(tup[0])
tup1 = (tup[0], tup[1])
print(tup1)
del tup1
# print(tup1)

print(len(tup))
print(tup + tup)
print(tup * 3)
print('math' in tup)
for x in tup:
    print(x)

oneItemTup = (1,)
print(oneItemTup)

list1 = [1,5,4]
print(list1)
tup1 = tuple(list1)
print(tup1)