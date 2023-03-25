# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_part = slow.next
        
        cur, prev = slow, None
        while cur:       
            cur.next, prev, cur = prev, cur, cur.next
            
        while head:
            ans = max(ans, prev.val + head.val)
            prev = prev.next
            head = head.next
            
        return ans