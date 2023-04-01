# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def helper(node):
            if not node:
                return
            if node.val == val:
                return helper(node.next)
            temp = helper(node.next)
            node.next = temp
            return node
        return helper(head)