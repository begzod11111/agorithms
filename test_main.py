import unittest
from main import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_push(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(len(x), 3)
        self.assertEqual(x[0], 1)
        self.assertEqual(x[1], 2)
        self.assertEqual(x[2], 3)

    def test_pop(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(x.pop(), 3)
        self.assertEqual(x.pop(), 2)
        self.assertEqual(x.pop(), 1)
        self.assertEqual(len(x), 0)

    def test_shift(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(x.shift(), 1)
        self.assertEqual(x.shift(), 2)
        self.assertEqual(x.shift(), 3)
        self.assertEqual(len(x), 0)

    def test_unshift(self):
        x = DoublyLinkedList()
        x.unshift(1)
        x.unshift(2)
        x.unshift(3)
        self.assertEqual(len(x), 3)
        self.assertEqual(x[0], 3)
        self.assertEqual(x[1], 2)
        self.assertEqual(x[2], 1)

    def test_get(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(x.get(0), 1)
        self.assertEqual(x.get(1), 2)
        self.assertEqual(x.get(2), 3)

    def test_count(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(1)
        x.push(3)
        self.assertEqual(x.count(1), 2)
        self.assertEqual(x.count(2), 1)
        self.assertEqual(x.count(3), 1)
        self.assertEqual(x.count(4), 0)

    def test_index(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        self.assertEqual(x.index(1), 0)
        self.assertEqual(x.index(2), 1)
        self.assertEqual(x.index(3), 2)

    def test_insert(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        x.insert(1, 4)
        self.assertEqual(len(x), 4)
        self.assertEqual(x[0], 1)
        self.assertEqual(x[1], 4)
        self.assertEqual(x[2], 2)
        self.assertEqual(x[3], 3)

    def test_remove(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        x.push(2)
        x.remove(2)
        self.assertEqual(len(x), 3)
        self.assertEqual(x[0], 1)
        self.assertEqual(x[1], 3)
        self.assertEqual(x[2], 2)

    def test_reverse(self):
        x = DoublyLinkedList()
        x.push(1)
        x.push(2)
        x.push(3)
        x.reverse()
        self.assertEqual(len(x), 3)
        self.assertEqual(x[0], 3)
        self.assertEqual(x[1], 2)
        self.assertEqual(x[2], 1)

if __name__ == '__main__':
    unittest.main()