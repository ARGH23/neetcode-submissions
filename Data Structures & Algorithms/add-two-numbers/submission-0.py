# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.carry = 0
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            total = self.carry
            if total == 0:
                return None
            else:
                nNode = ListNode(total)
                return nNode
        
        elif l1 == None:
            total = l2.val + self.carry
            self.carry = int(total/10)
            total = total%10

            nNode = ListNode(total)
            nNode.next = self.addTwoNumbers(l1, l2.next)
            return nNode

        elif l2 == None:
            total = l1.val + self.carry
            self.carry = int(total/10)
            total = total%10

            nNode = ListNode(total)
            nNode.next = self.addTwoNumbers(l1.next, l2)
            return nNode


        total = l1.val + l2.val + self.carry

        self.carry = int(total/10)
        total = total%10


        nNode = ListNode(total)
        nNode.next = self.addTwoNumbers(l1.next, l2.next)
        return nNode
        