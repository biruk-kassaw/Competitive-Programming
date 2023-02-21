# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        following = head
        previous = None
        
        while cur:
            following = following.next
            cur.next = previous
            previous = cur
            cur = following
        return previous