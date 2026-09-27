# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = float("-inf")
        def dfs(root):
            nonlocal maxPathSum
            if root == None:
                return 0
            
            left = max(dfs(root.left),0 )
            right = max(dfs(root.right),0)
            # Both sides 
            bothSides = root.val + left + right
            oneSide = root.val + max(left, right)
            maxPathSum = max(maxPathSum, bothSides)
            return oneSide
        dfs(root)
        return maxPathSum