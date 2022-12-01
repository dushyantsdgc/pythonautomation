# Normal List:

set1 = set()
for i in range(20):
    if i % 2 ==0:
        set1.add(i)
print(set1)


# With List Comprehension:

set2 = {i for i in range(20) if i % 2 == 0}
print(set2)