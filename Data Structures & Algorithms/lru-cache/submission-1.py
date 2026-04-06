class ListNode:

    def __init__(self, key=0, value = 0, next = None, prev =None):
        self.val = value
        self.key = key
        self.next = next
        self.prev = prev



class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.mp = {}
        self.cap = capacity


    def get(self, key: int) -> int:
        if self.mp.get(key):
            #first detatch the wires attached to the node im getting
            t1, t2 = self.mp[key].prev, self.mp[key].next
            t1.next, t2.prev = t2, t1
            #then reset the wires:
            self.mp[key].prev, self.mp[key].next = self.head, self.head.next
            self.head.next.prev =  self.mp[key]
            self.head.next = self.mp[key]
            return self.mp[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #put needs to check for dupes
        if key in self.mp:
            self.mp[key].val = value
            #first detach the pointers from the original place in map
            l = self.mp[key].prev
            r = self.mp[key].next
            l.next, r.prev = r, l
            self.insert(self.mp[key])
        else:
            self.mp[key] = ListNode(key,value)
            self.insert(self.mp[key])
            
        if len(self.mp)>self.cap:
            lru = self.tail.prev
            self.remove(self.tail.prev)
            del self.mp[lru.key]


    def remove(self, node):
        temp = node.next
        temp.prev = node.prev
        node.prev.next = temp 
    
    
    def insert(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
 
