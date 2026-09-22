# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0 
        maxval = root.val
        def dfs(root, maxval):
            nonlocal res
            if root == None:
                return

            # QUESTION 1:
            # Is root.val >= maxval?
            # If yes, what should happen to res?
            if root.val >= maxval:
                res += 1

            # QUESTION 2:
            # What should maxval become before
            # going to this node's children?
            maxval = max(root.val, maxval)

            dfs(root.left, maxval)
            dfs(root.right, maxval)
        dfs(root, maxval)
        return res
        