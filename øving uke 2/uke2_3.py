# Skriv en rekursiv funksjon intpow(x, n) som tar i mot to
# heltall, x og n, og beregner x ^ n.
# Sørg for å legge den i et program med flere testtilfeller
# for å teste at funksjonen din fungerer riktig

def intpow(x, n):
    if n == 0:
        return 1
    else:
        return x * intpow(x, n - 1)


for i in range(0,10):
    real_sum = i ** i   # innebygd funksjon for å regne opphøyd i
    intsum = intpow(i, i)
    print(intsum == real_sum)