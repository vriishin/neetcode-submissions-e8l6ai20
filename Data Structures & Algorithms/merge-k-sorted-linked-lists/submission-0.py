# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        sol = dummy
        while True:
            if not any(lists):
                break 
            lowest = ListNode(float('infinity'))
            lowest_i = -1
            for i, node in enumerate(lists):
                if node and lowest.val >= node.val:
                    lowest = node
                    lowest_i = i

            if lists[lowest_i]:
                lists[lowest_i] = lists[lowest_i].next 

            sol.next = lowest
            sol = sol.next
        return dummy.next
