import unittest
from øving_3 import øving_uke_3

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        stack = øving_uke_3.MyStack()

    def test_something(self):
        self.assertEqual(True, False)

    def test_stack_push(self):
        øving_uke_3.stack.push(3)



if __name__ == '__main__':
    unittest.main()
