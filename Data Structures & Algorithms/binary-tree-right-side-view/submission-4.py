# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def bfs(root):
            queue = deque()
            if root:
                queue.append(root)
            while queue:
                curLevel = []
                for i in range(len(queue)):
                    cur = queue.popleft()
                    
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    curLevel.append(cur.val)
                res.append(curLevel[-1])
        bfs(root)
        return res