import unittest
from collections import namedtuple
import csv
from innlevering_4.BinaryTreeNode import BinaryTreeNode

class MyTestCase(unittest.TestCase):

    def test_can_read_data_file(self):
        #Person = namedtuple("Person", "etternavn, fornavn, adresse, postnummer, poststed")
        Person = namedtuple('Person', ['etternavn', 'fornavn', 'adresse', 'postnummer', 'poststed'])

        for person in map(Person._make, csv.reader(open('Personer.dta', 'r'))):
            person = Person._make()

        # with open(Person._make, "Personer.dta", "r", encoding="ISO-8859-1") as file:
        #     for line in file:
        #         p = line.split(";")
        #         persons.append(p)  # lager en todimensjonal liste
        #
        # print(persons[0])

                #persons.append(p)  # lager en todimensjonal liste
        #for p in map(Persons._make, csv.reader(open('Personer.dta', 'r', encoding="ISO-8859-1"))):
         #   print(p.etternavn, p.fornavn)
          #  assert p.name != ""


if __name__ == '__main__':
    unittest.main()
