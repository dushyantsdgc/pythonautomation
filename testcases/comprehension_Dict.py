# Normal Dictionary:

dict1 = {}
for n in range(10):
    dict1[n] = n*2
print(dict1)


# With Dictionary Comprehension:

dict2 = {n:n*2 for n in range(10)}
print(dict2)