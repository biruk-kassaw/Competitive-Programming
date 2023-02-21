# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        if not head.next:
            return True
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = None
        
        cur = slow
        
        previous = None
        following = slow
        while cur:
            following = following.next
            cur.next = previous
            previous = cur
            cur = following
         
        while head and previous:
            if head.val != previous.val:
                return False
            head = head.next
            previous = previous.next
        return True
    