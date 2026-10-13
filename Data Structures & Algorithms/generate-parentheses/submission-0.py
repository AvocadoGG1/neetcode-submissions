class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(path):
            if len(path) == 2 * n:
                res.append("".join(path))
                return 
            open_count = path.count("(")
            close_count = path.count(")")
            if open_count < n:
                path.append("(")
                backtrack(path)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(path)
                path.pop()
            # invalid when () dont have matching
            
            
        backtrack([])
        return res
