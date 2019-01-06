def sum_list(lister):
    sum = 0
    for x in lister:
        sum += x
    
    print('Inner', sum)
    return sum


lister = [1, 2, 5, 2]
sum = sum_list(lister)

print('Outer', sum)