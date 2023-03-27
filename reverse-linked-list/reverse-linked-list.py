# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(cur, prev):
            if not cur.next:
                cur.next = prev
                return cur
            next_node = cur.next
            cur.next = prev
            return helper(next_node, cur)
        cur = head   
        if not head:
            return head
        return helper(cur, None)