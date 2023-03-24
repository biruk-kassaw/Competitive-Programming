# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        temp = dummy
        while l1 or l2:
            summ = 0
            if l1 and l2:
                summ = l1.val + l2.val + carry
            elif l2:
                summ = l2.val + carry
            else:
                summ = l1.val + carry
            if summ > 9:
                summ = summ - 10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(summ)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            temp.next = ListNode(1)
        
        return dummy.next