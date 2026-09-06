# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        if head.next == None:
            return


        length = 0

        lenh = head
        while lenh:
            length += 1
            lenh = lenh.next

        midrev = head
        for i in range(int((length+1)/2)):
            if i == int((length+1)/2) - 1:
                togo = midrev.next
                midrev.next = None
                midrev = togo
            else:
                midrev = midrev.next

        
        prev = None
        while midrev.next != None:
            togo = midrev.next
            midrev.next = prev
            prev = midrev
            midrev = togo
        midrev.next = prev

        toret = head
        final = toret
        o = head.next
        print(toret.val)

        while midrev != None:
            toret.next = midrev
            midrev = midrev.next
            toret = toret.next
            print(toret.val)
            if o != None:
                toret.next = o
                o = o.next
                toret = toret.next
                print(toret.val)
        
