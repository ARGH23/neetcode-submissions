# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solve(root):
    if root == None:
        return [0,-1001]
    
    #path value is 0 index, max is 1
    left = solve(root.left)
    right = solve(root.right)

    pvalue = root.val + max(left[0], right[0],0)
    maxi = max(root.val, left[1], right[1], root.val + left[0], root.val + right[0], root.val + left[0] + right[0])

    #print([pvalue, maxi])
    return [pvalue, maxi]


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return solve(root)[1]