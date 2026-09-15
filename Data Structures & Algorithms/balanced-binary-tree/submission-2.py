# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def preorder(root):
            nonlocal res
            # Base Case - had to change from None to zero
            if root == None:
                return 0
            lHeight = preorder(root.left) # dont add anymore vars no lHeight inside the def
            rHeight = preorder(root.right) 
            print(f"After for right: {rHeight}")
            print(f"After for right: {lHeight}")
            if abs(lHeight - rHeight) >= 2:
                print("Here")
                res = False
            return 1 + max(lHeight, rHeight) # Get the height of each subtree
        preorder(root)
        print(res)
        return res