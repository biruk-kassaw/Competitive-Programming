# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        dummy_s = ListNode(2)
        dummy_s_head = dummy_s
        
        dummy_l = ListNode(3)
        dummy_l_head = dummy_l
        
        cur = head
        
        while cur:
            if cur.val < x:
                dummy_s.next = cur
                dummy_s = dummy_s.next
            else:
                dummy_l.next = cur
                dummy_l = dummy_l.next
            cur = cur.next
        dummy_l.next = None
        dummy_s.next = None
        if not dummy_s_head.next or not dummy_l_head.next:
            return head
        
        
        head = dummy_s_head.next
        
        while dummy_s_head.next:
            dummy_s_head = dummy_s_head.next
        dummy_s_head.next = dummy_l_head.next
        
        
        return head
        
        
#         if head.val >= x:
            
#             cur = head
#             while cur and cur.next:
#                 if cur.next.val < x:
#                     less_node = cur.next
#                     cur.next = cur.next.next
#                     temp = head
#                     head = less_node
#                     less_node.next = temp
#                 cur = cur.next
#             return head
        
#         greater = head
        
#         while greater and greater.next:
#             if greater.next.val >= x:
#                 previous = greater
#                 cur = greater
#                 greater = greater.next
                
#                 while cur and cur.next:
#                     if cur.next.val < x:
                        
#                         less_node = cur.next
#                         print(less_node.val)
#                         cur.next = cur.next.next
#                         previous.next = less_node
#                         less_node.next = greater
#                         previous = less_node
#                     cur = cur.next
#                 return head
#             greater = greater.next
#         return head
            
            
            