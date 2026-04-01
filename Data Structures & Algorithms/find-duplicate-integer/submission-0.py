class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = 0
        for i in range(len(nums)):
            if seen & 1<<(nums[i]-1):
                return nums[i]
            seen |= 1<<(nums[i]-1)
        return 0
        