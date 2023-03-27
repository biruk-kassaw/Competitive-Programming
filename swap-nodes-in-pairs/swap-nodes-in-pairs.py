# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head):
            if not head or not head.next:
                return head
            
            next_next_node, next_node = head.next.next, head.next
            
            next_node.next = head
            head_next = helper(next_next_node)
            head.next = head_next
            
            return next_node        
        return helper(head)