# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        
        seen = set()
        while fast:
            if fast in seen:
                return True
            seen.add(fast)
            fast = fast.next
            
        return False