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
    
            level = 0
            while len(queue) > 0:
                curLevel = []
                print("level: ", level)
                for i in range(len(queue)):
                    curr = queue.popleft()
                    curLevel.append(curr.val)
                    print(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                res.append(curLevel[-1])
                level += 1
        bfs(root)
        return res