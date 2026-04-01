class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idx_stack = []
        res = [0]*len(temperatures)
        for idx,num in enumerate(temperatures):
            while idx_stack and num > temperatures[idx_stack[-1]]:
                target_idx = idx_stack.pop()
                res[target_idx] = idx - target_idx
            else:
                idx_stack.append(idx)
        return res
                