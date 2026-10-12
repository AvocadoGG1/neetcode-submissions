class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
       
        def backtrack(i, r, c):
            if i == len(word):
                return True 
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]):
                return False
            tmp = board[r][c]
            board[r][c] = "#"
            found = (backtrack(i + 1, r + 1, c) or backtrack(i + 1, r - 1, c) or backtrack(i + 1, r, c + 1) or backtrack(i + 1, r, c - 1))
            board[r][c] = tmp
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0, r, c):
                    return True
        return False
            
        