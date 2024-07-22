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
        self.length = 0
    
    def _get_el(self, value=None):
        current = self.head
        while current:
            if value is not None and current.value == value:
                return current
            current = current.next
        return None
    
    def __str__(self):
        current = self.head
        str_print = ''
        while current:
            str_print += f' {current.value},'
            current = current.next
        return "[ " + str_print + " ]"
    
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            last_el = self._get_el()
            last_el.next = new_node
            new_node.prev = last_el
        self.length += 1
        return self.length
    
    def pop(self):
        if self.head is None:
            return None
        last_el = self._get_el()
        if last_el.prev:
            last_el.prev.next = None
        else:
            self.head = None
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
        

