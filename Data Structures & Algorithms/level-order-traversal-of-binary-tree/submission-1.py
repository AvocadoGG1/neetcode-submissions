# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use BFS
        res = []
        def bfs(root):
            queue = deque()
            nonlocal res
           
            if root:
                queue.append(root)
            # else:
            #     # First case if root is empty
            #     return []
            level = 0
            while len(queue) > 0:
                currLevel = [] # this part
                
                # print("level: ", level)
                for i in range(len(queue)):
                    curr = queue.popleft()
                    currLevel.append(curr.val) # this part
                    # print(f"Val: {curr.val}")
                    
                    if curr.left:
                        queue.append(curr.left)
                    
                    if curr.right:
                        queue.append(curr.right)
                res.append(currLevel) # this part
                level += 1
        bfs(root)
        return res

        

        
        