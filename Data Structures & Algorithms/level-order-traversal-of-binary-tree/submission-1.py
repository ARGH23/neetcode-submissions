# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        answer = []


        queue = [root]
        nextqueue = []

        while queue:
            
            toadd = []

            while queue:
                x = queue.pop(0)
                toadd.append(x.val)
                if x.left != None:
                    nextqueue.append(x.left)
                if x.right != None:
                    nextqueue.append(x.right)
            
            answer.append(toadd)
            queue = nextqueue
            nextqueue = []
        
        return answer