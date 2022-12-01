# Nested List:

create_list1 = [[24, 30, 36], [28, 35, 42]]
for i in range(6, 8):
    for j in range(4, 7):
        pass

# With List Comprehension:

create_list2 = [[i*j for j in range(4, 7)] for i in range(6, 8)]
print(create_list2)