# Normal List:

create_list1 = []
for i in range(20):
    if i % 2 == 0:
        create_list1.append(i)
print(create_list1)


# With List Comprehension:

create_list2 = [i for i in range(20) if i % 2 == 0]
print(create_list2)