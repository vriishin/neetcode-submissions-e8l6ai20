# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse first, then iterate back through, delete nth while reversing, return.

        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp
        
        newHead = prev
        newPrev = None
        count =1

        while newHead: 
            if count == n:
              newHead = newHead.next if newHead.next else None
            if newHead:    
                temp = newHead.next
                newHead.next = newPrev
                newPrev = newHead
                newHead = temp

            
                
            count+=1
        
        return newPrev
