class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in dic:
                    dic[board[i][j]] = 1
                else:
                    dic[board[i][j]] += 1 
            if len(dic.values())!= 0 and max(list(dic.values()))>1:
                return False
        # check column
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in dic:
                    dic[board[j][i]] = 1
                else:
                    dic[board[j][i]] += 1 
            if len(dic.values())!= 0 and max(list(dic.values()))>1:
                    return False
        # check 3*3
        for k in range(0,9,3):
            for l in range(0,9,3):
                dic = {}
                for i in range(3):
                    for j in range(3):
                        row_idx = k + i
                        col_idx = l + j
                        if board[row_idx][col_idx] == ".":
                            continue
                        if board[row_idx][col_idx] not in dic:
                            dic[board[row_idx][col_idx]] = 1
                        else:
                            dic[board[row_idx][col_idx]] += 1 
                if len(dic.values())!= 0 and max(list(dic.values())) >1:
                    return False
        
        return True