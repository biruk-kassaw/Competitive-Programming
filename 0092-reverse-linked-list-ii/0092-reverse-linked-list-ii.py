# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        counter_left = 1
        start = head
        prev = ListNode(0)
        prev.next = head
        
        while counter_left < left:
            start = start.next
            prev = prev.next
            counter_left += 1
    
        last = start
        
        while counter_left < right:
            last = last.next
            counter_left += 1
            
        last_next = last.next
        last.next = None
        
        prev_Reverser = None
        following = start
        start_before_reverse = start
        while start:
            following = following.next
            start.next = prev_Reverser
            prev_Reverser = start
            start = following
        prev.next = prev_Reverser
        start_before_reverse.next = last_next
        
        if left == 1:
            head = prev.next
        
        return head
        
        