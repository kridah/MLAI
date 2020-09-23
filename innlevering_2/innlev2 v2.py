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
    print("Iterate fibonacci")
    # for fib in fibs:
    #    print(fib)


iter_fib()

fib_list = []


# kode for Oppgave 2 her, bruk flere celler hvis det trengs
def fibonacci(fib_max):
    f0, f1 = 0, 1
    while True:
        if (f0 >= fib_max):
            return
        yield f0
        fib_list.append(f0)
        f0, f1 = f1, f0 + f1


fib_max = 1000
fibs = fibonacci(fib_max)

#print("Fibonacci for f in fibs:")
#for f in fibs:
#    print(f)


    # kode for Oppgave 3 her, bruk flere celler hvis det trengs
    #     def fibonacci_list():
    #         fib_list = []
    #         f0, f1 = 0, 1
    #         while f0 < 1000:
    #             f0, f1 = f1, f0 + f1
    #             # print(f0)
    #             fib_list.append(f0)
    #         return fib_list

    # Bruker derfor alternativ måte for å sjekke hvilke tall som er like i de to listene
def is_fib(x):
    f0, f1 = 0, 1
    while True:
        if (f0 >= 1000):
            return
        #fib_list.append(f0)
        if x == f0:
            return True
        f0, f1 = f1, f0 + f1
    return False



ints = list(range(0, 1000))
print("fib",[i for i in ints if is_fib(i)])
