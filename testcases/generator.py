def sample(a, b):
    while a < b:
        yield a
        a += 1


result = sample(1, 5)
for i in result:
    print(i)