import unittest
from main import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_push(self):
        # Test push method
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(str(x), "1 <-> 2 <-> 3")

    def test_pop(self):
        # Test pop method
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(x.pop(), 3)
        self.assertEqual(str(x), "1 <-> 2")

    def test_shift(self):
        # Test shift method
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(x.shift(), 1)
        self.assertEqual(str(x), "2 <-> 3")

    def test_unshift(self):
        # Test unshift method
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        x.unshift(0)
        self.assertEqual(str(x), "0 <-> 1 <-> 2 <-> 3")

    def test_get(self):
        # Test get method
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(x.get(1), 2)
        self.assertEqual(x.get(2), 3)

if __name__ == '__main__':
    unittest.main()