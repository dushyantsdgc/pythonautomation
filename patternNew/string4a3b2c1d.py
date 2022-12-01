s=input("Enter some string :")#a4b3c2
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
finalO=''.join(sorted(output))
print(finalO)
