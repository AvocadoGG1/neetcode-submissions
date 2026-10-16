class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(path, j, i ):
            # Whole string is cut into palindromes, save it
            if j >= len(s):
                res.append(path.copy())
                return
            # Ran out of string with an unfinished piece, dead end
            if i >= len(s):
                return
            # Choice 1: cut here, if s[j..i] is a palindrome
            if s[j:i + 1] == s[j:i + 1][::-1]:
                path.append(s[j:i + 1])
                backtrack(path, i + 1, i + 1)
                path.pop()

            # Choice 2: don't cut, extend the current piece
            backtrack(path, j, i + 1)
        
        backtrack([], 0, 0)
        return res