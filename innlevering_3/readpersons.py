# kode her

thisdict = {
}

persons = []
with open("Personer.dta", "r", encoding="ISO-8859-1") as file:
    d = thisdict([line.split(";") for line in file])


print(len(thisdict))
