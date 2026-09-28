class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        # 用字典建立數字與字母的對應表，直覺又安全
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            # 1. 終止條件：當 index 走到 digits 的長度，代表湊滿一組了
            if index == len(digits):
                res.append("".join(path))
                return
            
            # 2. 取得當前數字對應的字串
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # 3. 迴圈遍歷該數字的所有可能字母
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)  # 處理下一個數字
                path.pop()                  # 撤銷選擇（回溯）
                
        backtrack(0, [])
        return res