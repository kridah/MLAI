from typing import NamedTuple

from innlevering_4.BinaryTree import BinaryTree
from innlevering_4.BinaryTreeNode import BinaryTreeNode

class Person(NamedTuple):
    etternavn: str
    fornavn: str
    adresse: str
    postnummer: int
    poststed: str

    def print_person(self):
        print(f"{self.fornavn} {self.etternavn} bor i {self.adresse}, {self.postnummer} {self.poststed}")

    def __str__(self):
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



persons = [
    Person("KRISTIANSEN","MORTEN KRISTIAN","LEINAHYTTA 36",7224,"MELHUS"),
    Person("OLDERVIK","SHARI LILL","KRÅKA 84",7437,"FEDJE"),
    Person("GJERSTAD","TORKJELL","HOSTELAND 2 83",1361,"ØSTERÅS"),
    Person("VESTLY SKIVIK","JAHN FREDRIK","LINNGÅRD 22",1451,"NESODDTANGEN")
    ]
# nodes = [
#     Person(etternavn="KRISTIANSEN",fornavn="MORTEN KRISTIAN",adresse="LEINAHYTTA 36",postnummer=7224,poststed="MELHUS"),
#     Person(etternavn="OLDERVIK",fornavn="SHARI LILL",adresse="KRÅKA 84",postnummer=7437,poststed="FEDJE"),
#     Person(etternavn="GJERSTAD",fornavn="TORKJELL",adresse="HOSTELAND 2 83",postnummer=1361,poststed="ØSTERÅS"),
#     Person(etternavn="VESTLY SKIVIK",fornavn="JAHN FREDRIK",adresse="LINNGÅRD 22",postnummer=1451,poststed="NESODDTANGEN")
#     ]

tree = BinaryTree()

# tree.insert(value="2")
# tree.insert(value="1")
# tree.insert(value="4")
# tree.insert(value="7")
# print(tree.find(key="2"))
# max_node = tree.findMax()
# print(max_node)

tree.insert("mordi")