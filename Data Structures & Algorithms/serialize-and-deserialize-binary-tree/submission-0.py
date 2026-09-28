# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec: 
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def dfs(root):
            if root is None:
                vals.append("#")
                return
            vals.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(vals)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # DFS
        tokens = iter(data.split(","))

        def dfs():
            val = next(tokens)          # read next token
            if val == "#":
                return None             # empty spot
            node = TreeNode(int(val))   # build a node
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        
    