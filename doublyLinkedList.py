from typing import Any


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.value)
        

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __getitem__(self, index: int) -> Any:
        return self.get(index)
    
    def __str__(self):
        if not self.head:
            return "Empty"
        current = self.head
        values_generator = (str(current.value) for current in self._iterate_from(self.head))
        return ' <-> '.join(values_generator)

    def _iterate_from(self, node):
        while node:
            yield node
            node = node.next
    
    def _bring_value(self, value):
        return Node(value)
    
    
    
    def push(self, value):
        new_node = self._bring_value(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self.length
    
    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            last_el = self.head
            self.head = None
            self.length -= 1
            return last_el.value
        else:
            last_el = self.tail
            self.tail = last_el.prev
            self.tail.next = None
        self.length -= 1
        return last_el.value
    
    def shift(self):
        if self.head is None:
            return None
        old_head = self.head
        self.head = old_head.next
        if self.head:
            self.head.prev = None
        self.length -= 1
        return old_head.value
    
    def unshift(self, value):
        new_node = self._bring_value(value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.length
    
    def __len__(self):
        return self.length
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.value
    
    def count(self, value):
        current = self.head
        count = 0
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count
    
    def index(self, value):
        current = self.head
        if current is None:
            return None
        for i in range(self.length):
            if current.value == value:
                return i
            current = current.next
        return None
        
        
    def insert(self, index: int, value):
        if index < 0 or index >= self.length:
            return None
        new_node = self._bring_value(value)
        current = self.head
        for i in range(index):
            current = current.next
        if current.prev:
            current.prev.next = new_node
            new_node.prev = current.prev
        new_node.next = current
        current.prev = new_node
        self.length += 1
        return self.length
        
    def remove(self, value, count=1):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                self.length -= 1
                count -= 1
            if count == 0:
                break
            current = current.next
        return self.length
    
    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head
        return self
        
        
        

x = DoublyLinkedList()

for i in range(10):
    x.push(i)
x.push(1)
# print(x.remove(1, 2))
x.reverse()
print(x)

