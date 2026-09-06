# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        single = head
        double = head.next

        while single != double:
            if single.next == None:
                return False
            else:
                single = single.next
            
            if double.next == None:
                return False
            else:
                double = double.next
                if double.next == None:
                    return False
                else:
                    double = double.next
        
        return True