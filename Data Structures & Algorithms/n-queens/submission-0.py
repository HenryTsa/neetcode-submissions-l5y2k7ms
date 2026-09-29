class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()       # 紀錄被佔用的行
        diag1 = set()      # 紀錄主對角線 (row - col)
        diag2 = set()      # 紀錄副對角線 (row + col)
        
        def backtrack(row, path):
            # 1. 終止條件：如果 row 走到了 n，代表每一行都成功放了皇后！
            if row == n:
                # 這裡要把 path（數字陣列）轉換成 LeetCode 要的棋盤字串格式
                board = []
                for c in path:
                    row_string = "." * c + "Q" + "." * (n - 1 - c)
                    board.append(row_string)
                res.append(board)
                return
            
            # 2. 嘗試在當前 row 的每一個 column 放置皇后
            for col in range(n):
                # 檢查：如果這一行、或者對角線已經被佔用了，就跳過
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # 做選擇（登記佔用）
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                path.append(col)
                
                # 進入下一行
                backtrack(row + 1, path)
                
                # 撤銷選擇（回溯，把登記拿掉）
                path.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                
        backtrack(0, [])
        return res