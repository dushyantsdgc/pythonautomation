# Normal Dictionary:

dict1 = {}
for n in range(10):
        if n % 2 == 0:
            dict1[n] = n * 2
print(dict1)


# With Dictionary Comprehension:

dict2 = {n:n*2 for n in range(10) if n % 2 == 0}
print(dict2)