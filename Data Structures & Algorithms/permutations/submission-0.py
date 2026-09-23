class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def swap(i,j):
            tempt = nums[i]
            nums[i] = nums[j]
            nums[j] = tempt
        def backtrack(start):
            if start == len(nums)-1:
                res.append(nums.copy())
            for i in range(start, len(nums)):
                swap(start,i)
                backtrack(start+1)
                swap(start,i)
        backtrack(0)
        return res

        