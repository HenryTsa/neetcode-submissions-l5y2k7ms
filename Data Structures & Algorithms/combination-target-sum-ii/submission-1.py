class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # 一定要先排序
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(path.copy()) # 直接放進去，不需要檢查 not in res
                return
            
            for i in range(start, len(candidates)):
                # 剪枝：如果超過 target，後面不用看了
                if target - candidates[i] < 0:
                    break
                
                # 【關鍵防重複機制】
                # 如果當前數字跟「前一個數字」一樣，且不是這一輪迴圈的第一個選項
                # 就直接跳過，避免產生重複的組合
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                path.append(candidates[i])
                backtrack(i + 1, path, target - candidates[i]) # 每個數字只能用一次，所以傳 i + 1
                path.pop()
                
        backtrack(0, [], target)
        return res