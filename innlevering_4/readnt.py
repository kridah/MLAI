from typing import NamedTuple


class Person(NamedTuple):
    etternavn: str
    fornavn: str
    adresse: str
    postnummer: int
    poststed: str

    def print_person(self):
        print(f"{self.fornavn} {self.etternavn} bor i {self.adresse}, {self.postnummer} {self.poststed}")


# Dette lager Person-objekter som man kan referere til med atributtene til klassen
def get_persons():
    return [
        Person("ELI", "KNUT OLAF", "RUSTAD S 14", 9775, "GAMVIK"),
        Person("TOLLEFSEN","ZULFIQAR ALI","EIRIK JARLS GATE 79",1305,"HASLUM")
    ]

def get_persons_from_file():
    persons = []
    with open("Personer.dta", "r", encoding="ISO-8859-1") as file:
        for line in file:
            p = line.split(";")
            persons.append(p)
        return persons


for person in get_persons_from_file():
    p = Person(person[0], person[1], person[2], person[3], person[4])
    print(p.fornavn)