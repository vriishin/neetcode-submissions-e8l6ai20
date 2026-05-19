class ListNode:

    def __init__(self, key=0, value = 0, next = None, prev =None):
        self.val = value
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next, self.tail.prev = self.tail, self.head

        self.mp = {}

        

    def get(self, key: int) -> int:
        if self.mp.get(key):
            self.remove(self.mp[key])
            self.insert(self.mp[key])
        
            return self.mp[key].val
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key].val = value
            l, r = self.mp[key].prev, self.mp[key].next
            l.next, r.prev = r, l
            self.insert(self.mp[key])
        
        else:
            self.mp[key] = ListNode(key, value)
            self.insert(self.mp[key])

        if len(self.mp)>self.cap:
            lru = self.tail.prev
            self.remove(self.tail.prev)
            del self.mp[lru.key]
        
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next, node.prev = None, None

    def insert(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head 



