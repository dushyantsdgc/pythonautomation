# Normal List:

create_list1 = []
for i in range(20):
    create_list1.append(i+1)
print(create_list1)


# With List Comprehension:

create_list2 = [i+1 for i in range(20)]
print(create_list2)