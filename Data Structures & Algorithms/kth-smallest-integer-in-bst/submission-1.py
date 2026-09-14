# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def solve(root, num, found):
            if found:
                return [num, found]

            if root == None:
                return [num, found]
            
            x = solve(root.left, num, found)

            num = x[0]
            found = x[1]

            num += 1
            if found:
                return [num, found]
            if num == k:
                return [num, root.val]
            x = solve(root.right, num, found)
            num = x[0]
            found = x[1]
            return [num, found]

        return solve(root, 0, None)[1]