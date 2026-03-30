# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first you find middle
        turtle, rabbit = head, head.next
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
        
        second_list = turtle.next
        prev = None
        turtle.next = None #splits the lists up

        # now reverse second half of list i.e. second list
        while second_list:
            temp = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = temp
        
        #prev is head of second list

        #then can add those in order

        # first second first second etc.

        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
     