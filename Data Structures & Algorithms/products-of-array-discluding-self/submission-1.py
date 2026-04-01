class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        suffix = [0]*len(nums)
        suffix.append(1)
        suffix[len(nums)-1] = nums[len(nums)-1]
        res = [0]*len(nums)
        for i,number in enumerate(nums):
            if i != 0:
                prefix[i]=(prefix[i-1] *nums[i])
        for i in range(len(nums)-2,-1,-1):
            suffix[i]= (suffix[i+1]*nums[i])
        print(prefix)
        print(suffix)
        for i in range(len(nums)):
            if i!=0:
                res[i] = suffix[i+1] * prefix[i-1]
            else:
                res[i] = suffix[i+1]
        return res