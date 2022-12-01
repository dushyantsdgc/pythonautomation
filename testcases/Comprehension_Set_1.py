# Normal List:

set1 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
set2 = set()
for i in set1:
    set2.add(i+1)
print(set2)


# With List Comprehension:
set3 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
set4 = {i+1 for i in set3}
print(set4)