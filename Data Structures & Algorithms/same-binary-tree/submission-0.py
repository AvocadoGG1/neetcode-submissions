# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are empty
        
        def isThisTheSameTree(root, root2):
            # 1. Are BOTH nodes None?
            #    What should I return?
            if root == None and root2 == None:
                return True
            # 2. Is ONLY ONE of them None?
            #    What should I return?
            if root == None or root2 == None:
                return False
            # 3. Both nodes exist.
            #    Are their values different?
            #    What should I return?
            if root.val != root2.val:
                return False
            # 4. Values match.
            #    Check the left pair
            left = isThisTheSameTree(root.left, root2.left)

            #    Check the right pair
            right = isThisTheSameTree(root.right, root2.right)

            # 5. What needs to be true about BOTH left and right?
            return left and right
        # Start here
        isThisTheSameTree(p, q)
        # Return res  
        res = isThisTheSameTree(p, q) 
        return res