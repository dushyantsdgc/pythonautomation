def sample(a, b):
    while a < b:
        yield a
        a += 1


result = sample(1, 5)
# lst = list(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))