f = open("sample.txt", "r")
quote = f.read()
print(quote)

print(f.read()) 

f.seek(0)

print(f.read()) 

f.close()