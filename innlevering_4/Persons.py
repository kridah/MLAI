from typing import NamedTuple

persons = []
class Person(NamedTuple):
    etternavn: str
    fornavn: str
    adresse: str
    postnummer: int
    poststed: str

    def __str__(self):
        print(f"{self.fornavn} {self.etternavn} bor i {self.adresse}, {self.postnummer} {self.poststed}")

    def get_persons_from_file(self):

        with open("Personer.dta", "r", encoding="ISO-8859-1") as file:
            for line in file:
                p = line.split(";")
                persons.append(p)
            return persons
