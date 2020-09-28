# kode her

persons = []
with open("Personer.dta", "r", encoding="ISO-8859-1") as file:
    for line in file:
        d = line.split(";")
        persons.append(d)


postnummer_set = set()
for i in range(100000):
    postnummer_set.add(persons[i][3])

print(len(postnummer_set))
