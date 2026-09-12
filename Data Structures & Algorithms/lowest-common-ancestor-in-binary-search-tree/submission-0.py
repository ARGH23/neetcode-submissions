# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root, p, q, seen):
    if root == None:
        return []
    
    rightseen = solve(root.right, p, q, seen)
    leftseen = solve(root.left, p, q, seen)

    if len(rightseen) == 3:
        return rightseen
    if len(leftseen) == 3:
        return leftseen
    
    seen = rightseen + leftseen

    if root == p or root == q:
        seen.append(root.val)

    if len(seen) == 2:
        seen.append(root)
    
    print(seen)
    return seen



class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        x = solve(root, p, q, [])
        return x[-1]