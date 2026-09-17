# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # Check if valid tree
            def isSameTree(root, subRoot):
                # TODO:
                # both None?             -> True
                # only one None?         -> False
                # values different?      -> False
                if root == None and subRoot == None:
                    return True
                if root == None or subRoot == None:
                    return False
                if root.val != subRoot.val:
                    return False
                
                # Then recursively compare:
                # left with left
                # right with right
                left = isSameTree(root.left, subRoot.left)
                right = isSameTree(root.right, subRoot.right)
                return left and right
            # Search for the potiental beginning of subtree
            def isThisASubtree(root, subRoot):
                if root == None and subRoot == None:
                    return True
                if root == None or subRoot == None:
                    return False
                if root.val == subRoot.val:
                    if isSameTree(root, subRoot):
                        return True
                leftSubtree = isThisASubtree(root.left, subRoot)
                rightSubtree = isThisASubtree(root.right, subRoot)

                return leftSubtree or rightSubtree
            
            res = isThisASubtree(root, subRoot)
            return res