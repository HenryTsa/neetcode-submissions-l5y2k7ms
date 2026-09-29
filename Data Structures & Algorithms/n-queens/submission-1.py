class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        diagonal_1 = set()
        diagonal_2 = set()
        
        def backtrack(row,path):
            if row == n:
                board = []
                print(path)
                for c in path:
                    board.append('.'*c + 'Q' + '.'*(n-c-1))
                res.append(board)
                return 
            for j in range(n):
                if j not in col and j+row not in diagonal_1 and j-row not in diagonal_2:
                    path.append(j)
                    col.add(j)
                    diagonal_1.add(j+row)
                    diagonal_2.add(j-row)
                    backtrack(row+1,path)
                    path.pop()
                    col.remove(j)
                    diagonal_1.remove(j+row)
                    diagonal_2.remove(j-row)
              
        backtrack(0, [])
        return res