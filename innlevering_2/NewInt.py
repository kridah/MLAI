class NewInt(int):
    def __init__(self, range_max):
        super().__init__()
        self.sequence = list(range(0, range_max))
        self.range_max = range_max
        self.index = 0

    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        result = self.sequence[self.index]
        self.index += 1
        return result

    def __iter__(self):
        return self

    def is_fib(self):
        f0, f1 = 0, 1
        while True:
            if f0 > self.range_max:
                return False
            if self == f0:
                return True
            f0, f1 = f1, f0 + f1

# for i in range(0, 100):
#    i = NewInt(i)
#    print(i.is_fib())
#    print(str(i))


# %timeit pass
compared_fibonaccis = [x for x in range(0, 1000) if NewInt(x).is_fib()]

print(compared_fibonaccis)
