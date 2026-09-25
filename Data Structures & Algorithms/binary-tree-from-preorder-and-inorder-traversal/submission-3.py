# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, preorder:List[int], left:int, right:int)->TreeNode:
        if left > right or self.preorder_index >= len(preorder):
            return None
        
        inorder_node_position = self.inorder_traversal_position[preorder[self.preorder_index]]
        node = TreeNode(preorder[self.preorder_index])

        
        
        self.preorder_index += 1
        node.left = self.dfs(preorder, left, inorder_node_position - 1)

        if node.left is None:
            self.preorder_index -= 1

        self.preorder_index += 1
        node.right = self.dfs(preorder, inorder_node_position + 1, right)

        if node.right is None:
            self.preorder_index -= 1

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_traversal_position = defaultdict(int)
        self.preorder_index = 0

        for i, num in enumerate(inorder):
            self.inorder_traversal_position[num] = i
        
        return self.dfs(preorder, 0, len(preorder)-1)
