class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(r,c,step):
            if step == len(word):
                return True
            if r >= rows or c>= cols or r<0 or c<0 or board[r][c] != word[step]:
                return False
            tempt = board[r][c]
            board[r][c] = '#'
            Found = (backtrack(r+1,c,step+1) or backtrack(r,c+1,step+1) or 
                     backtrack(r-1,c,step+1) or backtrack(r,c-1,step+1))
            board[r][c] = tempt
            return Found
        # 矩陣中的每一個格子都有可能是起點
        for i in range(rows):
            for j in range(cols):
                # 從 (i, j) 開始找 word 的第 0 個字元
                if backtrack(i, j, 0):
                    return True
                    
        return False