# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        start = head
        cur = head.next
        
        while cur:
            while cur and  cur.val == start.val:
                cur = cur.next
            start.next = cur
            start = cur
            if cur:
                cur = cur.next
        return head