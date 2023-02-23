# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first_pointer = head
        second_pointer = head
        prev = ListNode(0)
        prev.next = head
        
        for i in range(n-1):
            second_pointer = second_pointer.next
            
        while second_pointer.next:
            prev = prev.next
            second_pointer = second_pointer.next
       
        first_pointer = prev.next
        
        if first_pointer == head:
            return prev.next.next
        
        
        prev.next = first_pointer.next
        print(head.val)
        
        return head