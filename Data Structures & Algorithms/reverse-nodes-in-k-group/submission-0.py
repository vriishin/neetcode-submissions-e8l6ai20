# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head 
        dummy = ListNode()
        groupPrev = dummy
        while True:
            temp = 1
            while fast and temp<k:
                fast = fast.next
                temp+=1
            if fast is None: break
            groupNext = fast.next
            groupStart = slow

            #reverse between slow and fast but how to manage the pointers....
            #reverse LL remember prev beocmes new head:
            prev = fast.next
            while slow is not groupNext:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp

            
            
            groupPrev.next = prev 
            groupPrev = groupStart

            fast = slow = groupNext

            
        return dummy.next
            
        