# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def solve(root, p, q, seen):
#     if root == None:
#         return []
    
#     rightseen = solve(root.right, p, q, seen)
#     leftseen = solve(root.left, p, q, seen)

#     if len(rightseen) == 3:
#         return rightseen
#     if len(leftseen) == 3:
#         return leftseen
    
#     seen = rightseen + leftseen

#     if root == p or root == q:
#         seen.append(root.val)

#     if len(seen) == 2:
#         seen.append(root)
    
#     print(seen)
#     return seen



class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
            return root
        
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root





