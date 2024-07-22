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
    
    def _get_last_el(self):
        current = self.head
        if current is None:
            return None
        while current.next:
            current = current.next
        self.tail = current
        return current
    
    def __str__(self):
        current = self.head
        if current is None:
            return "[ ]"
        str_print = ''
        while current:
            str_print += f' {current.value},'
            current = current.next
        return "[ " + str_print + " ]"
    
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.tail is None:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node
        else:
            last_el = self.tail
            last_el.next = new_node
            new_node.prev = last_el
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
        new_node = Node(value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.length
    
    def __len__(self):
        return self.length
    
    def get(self, index):
        if 0 < index <= self.length:
            if index < self.length // 2:
                current = self.head
                for i in range(index):
                    current = current.next
                return current
            else:
                current = self.tail
                for i in range(self.length - index - 1):
                    current = current.prev
                return current
        return None
    
    def count(self, value):
        current = self.head
        count = 0
        if current is None:
            return count
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
        

x = DoublyLinkedList()

for i in range(10):
    x.push(i)
x.push(1)

print(x.count(1))

