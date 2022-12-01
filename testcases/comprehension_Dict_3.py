# Normal Dictionary:

dict1 = {}
for n in range(10):
        if n % 2 == 0:
            dict1[n] = n
        else:
            dict1[n] = 'invalid'
print(dict1)


# With Dictionary Comprehension:

dict2 = {n: (n if n%2==0 else 'invalid') for n in range(10)}
print(dict2)