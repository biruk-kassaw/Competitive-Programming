# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        
        temp = right.next
        right.next = None
        
        right = temp
        
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        return self.merge(left_sorted, right_sorted)
        
    def merge(self, left_part, right_part):

        new_head = ListNode(0)
        cur = new_head

        while left_part and right_part:

            if left_part.val < right_part.val:
                cur.next = left_part
                cur = cur.next
                left_part = left_part.next
            else:
                cur.next = right_part
                cur = cur.next
                right_part = right_part.next

        if left_part:
            cur.next = left_part

        if right_part:
            cur.next = right_part

        return new_head.next

            
            
            
            