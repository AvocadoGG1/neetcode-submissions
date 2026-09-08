class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
   
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.hashmap = {}
        self.capacity = capacity
        
    def move_to_mru(self, node):
        # tail case
        if node != self.tail:

            # head case
            if node == self.head:
                self.head = self.head.next
                self.head.prev = None

            # middle case
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            # add node to end
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = None
    def add_to_mru(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        node.next = None
        
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap.get(key)
        self.move_to_mru(node)
        return node.val
        
                
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.move_to_mru(node)
        else: 
            node = Node(key, value)
            self.hashmap[key] = node
            self.add_to_mru(node)
        if len(self.hashmap) > self.capacity:
            lru = self.head

            del self.hashmap[lru.key]

            self.head = self.head.next
            self.head.prev = None
