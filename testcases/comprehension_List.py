# Normal List:

create_list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
create_list2 = []
for i in create_list1:
    create_list2.append(i+1)
print(create_list2)


# With List Comprehension:
create_list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
create_list3 = [i+1 for i in create_list1]
print(create_list3)