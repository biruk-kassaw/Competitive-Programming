# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not list1 or not list2:
            return list2 or list1
        
        list1_pt = list1
        list2_pt = list2
        if list1.val < list2.val:
            head = list1
            list1_pt = list1_pt.next
        else:
            head = list2
            list2_pt = list2_pt.next
        sorter = head
        print(head.val)
        while list1_pt and list2_pt:
            if list1_pt.val < list2_pt.val:
                sorter.next = list1_pt
                list1_pt = list1_pt.next
            else:
                sorter.next = list2_pt
                list2_pt = list2_pt.next
            sorter = sorter.next
        if list1_pt:
            sorter.next = list1_pt
        if list2_pt:
            sorter.next = list2_pt
            
        return head