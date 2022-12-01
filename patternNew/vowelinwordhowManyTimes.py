word=input("Enter a string :")
vowel={'a','e','i','o','u'}
d1={}
for x in word:
    if x in vowel:
        d1[x]=d1.get(x,0)+1
for k,v in sorted(d1.items()):
    print(k, "occureds", v, "times")
