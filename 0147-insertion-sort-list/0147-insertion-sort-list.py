# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"))
        dummy.next = head
        
        prev = head
        cur = head.next
        
        while cur:
            if cur.val >= prev.val:
                cur = cur.next
                prev = prev.next
                continue
            temp = dummy
            
            while temp.next.val < cur.val:
                temp = temp.next
                
            prev.next = cur.next
            cur.next = temp.next
            temp.next = cur
            cur = prev.next
            
        return dummy.next
            
                