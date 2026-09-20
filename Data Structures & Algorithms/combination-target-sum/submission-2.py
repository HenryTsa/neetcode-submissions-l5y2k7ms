class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start,path,target):
            #print(path,target)
            if target < 0:
                return 
            elif target == 0:
                if path not in res:
                    res.append(path.copy())
                return 
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i,path,target-nums[i])
                path.pop()
                if target-nums[i]<0:
                    continue
        backtrack(0,[],target)
        return res
