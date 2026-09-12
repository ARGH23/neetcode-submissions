# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root, maxi):
    if root == None:
        return 0

    count = 0
    if root.val >= maxi:
        count += 1
        maxi = root.val
    
    return count + solve(root.left, maxi) + solve(root.right, maxi)

    
    


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return solve(root, -101)