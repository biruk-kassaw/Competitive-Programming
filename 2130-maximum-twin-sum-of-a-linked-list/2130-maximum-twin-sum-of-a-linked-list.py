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
        slow.next = None
        
        prev = None
        cur = second_part
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        while head:
            ans = max(ans, prev.val + head.val)
            prev = prev.next
            head = head.next
            
        return ans