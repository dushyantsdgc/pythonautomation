s=input("Enter some string :")
d={}
v={'a','e','i','o','u','A','E','I','O','U'}

for ch in s:
    if ch in v:
        d[ch]=d.get(ch,0)+1

for k,v in d.items():
    print("{} ocuurs {} times".format(k,v))