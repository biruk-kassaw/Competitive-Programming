# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even_head = head.next
        odd_iterator = head
        even_iterator = even_head
        
        while even_iterator and even_iterator.next and odd_iterator and odd_iterator.next:
            odd_iterator.next = even_iterator.next
            even_iterator.next = odd_iterator.next.next
            
            odd_iterator = odd_iterator.next
            even_iterator = even_iterator.next
        odd_iterator.next = even_head
        
        return head