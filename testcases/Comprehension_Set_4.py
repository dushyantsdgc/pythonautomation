# Normal List:

set1 = set()
for i in range(10):
    if i % 2 ==0:
        set1.add(i)
    else:
        set1.add(i * 1000)
print(set1)


# With List Comprehension:

set2 = {i if i % 2 == 0 else i*1000 for i in range(10)}
print(set2)