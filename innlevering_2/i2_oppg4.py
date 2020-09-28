class NewInt(int):
    def __init__(self, range_max):
        super().__init__()
        self.index = 0


def fibonacci(fib_max):
    f0, f1 = 0, 1
    while True:
        if (f0 >= fib_max): return
        yield f0
        f0, f1 = f1, f0 + f1


fib_set = set()
fibs = fibonacci(100_0000)
for f in fibs:
    fib_set.add(f)

int_list = [NewInt(i) for i in range(1000000)]
compared_fibonaccis = [i for i in int_list if i in fib_set]

print(compared_fibonaccis)
