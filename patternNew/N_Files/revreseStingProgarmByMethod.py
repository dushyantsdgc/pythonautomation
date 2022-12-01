s=input("Enter a string :")
temp_p=s
def reverseString(str1):
    global str2
    str2=str1[::-1]
    print("revresea o string ",str2)


reverseString(s)
if temp_p==str2:
    print("Palindeom")
else:
    print("NOT PALi")