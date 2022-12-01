# Normal List:

create_list1 = []
for i in range(20):
    if i % 2 == 0:
        create_list1.append(i)
    else:
        create_list1.append('invalid')
print(create_list1)


# With List Comprehension:

create_list2 = [i if i % 2 == 0 else 'invalid' for i in range(20)]
print(create_list2)