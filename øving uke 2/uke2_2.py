# Gjennomfør et eksperiment for å bevise at produktet med to tall ikke er
# avhengig av størrelsen på de to tallene som multipliseres.
# Skriv et program som plottar resultatene av å multiplisere antall i
# forskjellige størrelser sammen.
# Hint: For å få en gode data om dette kan det være lurt å gjøre mer enn en av
# disse multiplikasjonene og sette dem i gang som en gruppe siden en
# multiplikasjon skjer ganske raskt på en datamaskin.
# Kontroller at det virkelig er en O (1) -operasjon. Ser du noen avvik?

import datetime as date
import random
import numpy as np
import matplotlib.pyplot as plt


spent_time = []
result = []

# multipliserer to tilfeldige tall i range 1, 10000
# tiden ligger mellom 1-5 mikrosekund
# det ser ut til å være minimal økning i tiden selv ved mangedobling
def multiplier(rnd):
    start = date.datetime.now()
    result.append(rnd * (rnd * rnd))
    end = date.datetime.now()
    spent = end - start
    spent_time.append(spent)
    for s in range(len(spent_time)):
        print("Spent time: ", str(spent_time[s]), "Result: ", print(result[s]))


for i in range(1, 10):
    rnd = np.random.randint(1, 100)
    multiplier(rnd)


