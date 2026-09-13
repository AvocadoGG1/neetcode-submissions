# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        maxDiameter = 0
        def preorder(root):
            nonlocal maxDiameter
            if root == None:
                return 0
            l = preorder(root.left)
            r = preorder(root.right)
            # confusing part
            maxDiameter = max(maxDiameter, l + r)
            return 1 + max(l, r)
        
        preorder(root)

        return maxDiameter