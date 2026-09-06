# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        
        head = None
        first = None

        while list1 and list2:
            if list1.val < list2.val:
                if head:
                    head.next = list1
                    list1 = list1.next
                    head = head.next
                else:
                    head = list1
                    list1 = list1.next
                    first = head
            else:
                if head:
                    head.next = list2
                    list2 = list2.next
                    head = head.next
                else:
                    head = list2
                    list2 = list2.next
                    first = head
        
        if list1:
            while list1:
                head.next = list1
                head = head.next
                list1 = list1.next
        elif list2:
            while list2:
                head.next = list2
                head = head.next
                list2 = list2.next
        
        return first