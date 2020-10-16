import unittest
from typing import NamedTuple
from innlevering_4.BinaryTree import BinaryTree
from innlevering_4.BinaryTreeNode import BinaryTreeNode


class Person(NamedTuple):
    etternavn: str
    fornavn: str
    adresse: str
    postnummer: int
    poststed: str


class BstTest(unittest.TestCase):
    '''
        Bruker egendefinert array med Person-objekter for kunne gjennomføre testene hurtig og effektivt.
    '''

    # BUG: Kan ikke kjøre alle tester i ett. Noen av testene gir feil.
    # Kan fikses ved å kjøre de de aktuelle testene individuelt.
    tree = BinaryTree()
    minPerson = Person("GJERSTAD", "TORKJELL", "HOSTELAND 2 83", 1361, "ØSTERÅS")
    maxPerson = Person("VESTLY SKIVIK", "JAHN FREDRIK", "LINNGÅRD 22", 1451, "NESODDTANGEN")
    persons = [
        Person("KRISTIANSEN", "MORTEN KRISTIAN", "LEINAHYTTA 36", 7224, "MELHUS"),
        Person("OLDERVIK", "SHARI LILL", "KRÅKA 84", 7437, "FEDJE"),
        Person("GJERSTAD", "TORKJELL", "HOSTELAND 2 83", 1361, "ØSTERÅS"),
        Person("VESTLY SKIVIK", "JAHN FREDRIK", "LINNGÅRD 22", 1451, "NESODDTANGEN")
    ]

    # Legger personobjekter (4 stk) fra arrayet persons inn i treet.
    def setUp(self) -> None:
        super().setUp()
        for p in self.persons:
            self.tree.insert(value=p)

    # nullstiller treet
    def tearDown(self) -> None:
        super().tearDown()
        self.persons.clear()

    def test_can_read_data_file(self):
        persons_in_file = []
        with open("Personer.dta", "r", encoding="ISO-8859-1") as file:
            for line in file:
                person = line.split(";")
                persons_in_file.append(person)
        self.assertEqual(len(persons_in_file), 100_000)

    def test_insert_duplicate_node(self):
        person = Person("REMLO","KIM ANDRE","SANDFLATA 71",5648,"HOLMEFJORD")
        with self.assertRaises(Exception):
            self.tree.insert(self.minPerson)

    def test_insert(self):
        person = Person("REMLO","KIM ANDRE","SANDFLATA 71",5648,"HOLMEFJORD")
        node = BinaryTreeNode(person)
        self.assertEqual(node, self.tree.insert(value=person))

    def test_delete_min(self):
        node = BinaryTreeNode(self.minPerson)
        self.assertEqual(node, self.tree.deleteMin())

    def test_delete_max(self):
        node = BinaryTreeNode(self.maxPerson)
        self.assertNotEqual(node, self.tree.deleteMax())

    def test_is_greater_than(self):
        self.assertGreater(self.tree.findMax(), self.tree.findMin())

    def test_is_greater_or_equal(self):
        self.assertGreaterEqual(self.tree.findMax(), self.tree.findMax())

    def test_is_less_than(self):
        self.assertLess(self.tree.findMin(), self.tree.findMax())

    def test_is_less_or_equal(self):
        self.assertLessEqual(self.tree.findMin(), self.tree.findMax())
        self.assertLessEqual(self.tree.findMin(), self.tree.findMin())

    ## Disse testene må kjøres individuelt ##
    def test_delete_node(self):
        self.persons.clear()
        person = Person("REMLO","KIM ANDRE","SANDFLATA 71",5648,"HOLMEFJORD")
        node = BinaryTreeNode(person)
        self.tree.insert(value=person)
        self.assertEqual(node, self.tree.delete(key=person))

    def test_find(self):
        node = BinaryTreeNode(self.persons[0])
        self.assertEqual(node, self.tree.find(key=self.persons[0]))

    def test_findMax(self):
        node = BinaryTreeNode(self.maxPerson)
        self.assertEqual(self.tree.findRightMost(node), self.tree.findMax())

    def test_findMin(self):
        node = BinaryTreeNode(self.minPerson)
        self.assertEqual(self.tree.findLeftMost(node), self.tree.findMin())

    def test_delete_min_when_root(self):
        self.persons.clear()
        person = Person("REMLO", "KIM ANDRE", "SANDFLATA 71", 5648, "HOLMEFJORD")
        self.tree.insert(value=person)
        self.assertEqual(self.tree.find(self.minPerson), self.tree.deleteMin())

    def test_insert(self):
        self.persons.clear()
        for p in self.persons:
            node = BinaryTreeNode(p)
            self.tree.insert(value=p)
            self.assertEqual(node, self.tree.find(p))  # for hver insert, sjekk at objektet finnes i treet

if __name__ == '__main__':
    unittest.main()
