class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # (0,0)  , (2,3) -> 
        l_row,r_row = 0,len(matrix)-1
        l_col,r_col = 0,len(matrix[0])-1
        target_row = 0
        while l_row <= r_row :
            mid_row = int((l_row+r_row) / 2)
            #print(l,r,mid)
            if matrix[mid_row][0] > target:
                r_row = mid_row - 1
            elif matrix[mid_row][0] < target:
                target_row = mid_row
                l_row = mid_row + 1
            else:
                return True
        # print(target_row)
        while l_col <= r_col:
            mid_col = int((l_col+r_col)/2)
            if matrix[target_row][mid_col] == target:
                return True
            elif matrix[target_row][mid_col] < target:
                l_col = mid_col + 1
            else:
                r_col = mid_col - 1
        return False