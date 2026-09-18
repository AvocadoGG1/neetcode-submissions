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
            nonlocal descendant
            if p.val < root.val and q.val < root.val: # Both in left subtree
                return preorder(root.left, p, q)
                # if p.val < q.val:
                #     descendant = preorder(root, p, root.right)
                # else:
                #     descendant = preorder(root, p, root.left)
                # return descendant
            elif p.val > root.val and q.val > root.val: # Both in right subtree
                return preorder(root.right, p, q)
            else:
                return root
                # elif root.val == q.val:
                #     if q.val < p.val:
                #         descendant = preorder(root, root.right, q)
                #     else:
                #         descendant = preorder(root, root.left, q)
                #     return descendant

            return descendant
        res = preorder(root, p, q)
        return res