class yrange:
    def __init__(self, n):
        self.i=10
        self.n=5

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.n:
            raise StopIteration()
        else:
            i = self.i
            self.i -= 1
            return i

num = yrange(1)
for j in num:
    print(j)