class IterateFibonacci:
    def __init__(self, fib_max):
        self.fib_max = fib_max
        self.f0 = 0
        self.f1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.f0
        if fib >= self.fib_max:
            raise StopIteration
        self.f0, self.f1 = self.f1, self.f0 + self.f1
        return fib


fib_max = 1000


def iter_fib():
    fibs = IterateFibonacci(fib_max)
    for fib in fibs:
        print(fib)


iter_fib()