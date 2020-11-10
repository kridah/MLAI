# Din kode skrives her:
import pandas as pd
from collections import namedtuple
from innlevering_5.BinaryTree import BinaryTree


columnnames = ['etternavn', 'fornavn', 'adresse', 'postnr', 'poststed']
df = pd.read_csv("Personer.dta", encoding="ISO-8859-1", names=columnnames, header=None, sep=";")
person = namedtuple("Person",["etternavn", "fornavn", "adresse", "postnr", "poststed"])

tree = BinaryTree()

def tuplefy(lastname="", firstname="", adress="", postalcode="", postal=""):
    return person(etternavn=lastname, fornavn=firstname, adresse=adress, postnr=postalcode, poststed=postal)

persons = [tuplefy(lastname, firstname, adress, postalcode, postal)
for lastname, firstname, adress, postalcode, postal
in zip(df["etternavn"], df["fornavn"], df["adresse"], df["postnr"], df["poststed"])]

for p in persons:
    tree.insert(value=p)

# 1, 10, 100, 1000, 10000, 100000
# level = n-1
levels = [0, 9, 99, 999, 9999, 99999]
for index in levels:
    print("nivå ", (tree.find(persons[index]).level), " :: ", tree.find(persons[index]).value)

# Din kode fore rekursive delete kan du legge inn som kommentar i denne koden, samtidig som du endrer i BinaryTree
#
# Din kode for slettingen (del B) skrives her:
tree.delete_recursive(persons[999])
tree.delete_recursive(persons[9999])
# Skal nå få none på disse to nivåene
for index in levels:
    node = tree.find(persons[index])
    # hvis det finnes noder på nivået
    if node:
        print("nivå ", node.level, " :: ", node.value)
    # ingen noder på nivået
    else:
        print("Ingen noder funnet på nivå", index + 1)



levels = [7, 49, 399, 2299, 7999, 49998, 74999]
for index in levels:
    print("nivå ", tree.find(persons[index]).level, " :: ", tree.find(persons[index]).value)


# dictionary
levels = {}
def count_levels(node = None):
    if not node:
        count_levels(tree._root)
    else:
        try:
            levels[node.level] += 1
        except KeyError:
            levels[node.level] = 1
        if node.left:
            count_levels(node.left)
        if node.right:
            count_levels(node.right)

count_levels()

for (level, count) in levels.items():
    print("nivå", level, "antall: ", count)