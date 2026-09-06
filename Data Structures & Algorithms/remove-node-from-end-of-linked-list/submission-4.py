# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        lenh = head


        while lenh != None:
            length += 1
            lenh = lenh.next
        
        if length == 1:
            head = None
            return head
        if length == n:
            head = head.next
            return head

        torem = head
        for i in range(length - n - 1):
            torem = torem.next
        
        torem.next = torem.next.next
        return head