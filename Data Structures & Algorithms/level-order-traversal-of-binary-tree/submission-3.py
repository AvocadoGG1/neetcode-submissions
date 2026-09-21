# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use BFS
        if root is None:
            return []

        queue = []
        queue.append(root)
        holder = []
        result = []

        while queue:
            holder = []

            for _ in range(len(queue)):
                temp = queue.pop(0)
                holder.append(temp.val)

                if temp.left is not None:
                    queue.append(temp.left)

                if temp.right is not None:
                    queue.append(temp.right)
            
            result.append(holder)

        return result
        

        
        