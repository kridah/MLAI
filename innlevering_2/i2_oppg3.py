class NewInt(int):
    def __init__(self, range_max):
        super().__init__()
        self.index = 0

    def is_fib(self):
        f0, f1 = 0, 1
        while True:
            if f0 > 100_000:
                return False
            if self == f0:
                return True
            f0, f1 = f1, f0 + f1


int_list = [NewInt(i) for i in range(100000)]
compared_fibonaccis = [x for x in int_list if x.is_fib()]

print(compared_fibonaccis)
