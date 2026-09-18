# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Using DFS
        descendant = TreeNode(0)
        def preorder(root, p, q):
            if p.val < root.val and q.val < root.val: # Both in left subtree
                return preorder(root.left, p, q) # Only move root
            elif p.val > root.val and q.val > root.val: # Both in right subtree
                return preorder(root.right, p, q) 
            else: 
                return root  # They split, OR root itself is p/q
            return descendant 
        return preorder(root, p, q)