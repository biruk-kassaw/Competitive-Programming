# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        seen = {}
        
        start = head
        while start:
            while stack and start.val > stack[-1].val:
                seen[stack.pop()] = start.val
            stack.append(start)
            start = start.next
            
        start = head
        while start:
            ans.append(seen.get(start,0))
            start = start.next
        return ans