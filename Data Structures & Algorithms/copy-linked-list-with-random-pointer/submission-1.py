"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        curr = head
        while curr:
            temp = Node(curr.val)
            mp[curr] = temp
            curr = curr.next
        
        curr2 = head
        sol = mp[curr2] if curr2 else None
        while curr2:
            mp[curr2].next = mp[curr2.next] if curr2.next else None
            mp[curr2].random = mp[curr2.random] if curr2.random else None
            curr2 = curr2.next
            #how do i lookup hashmap entries based on their node value....



            
        
        return sol
