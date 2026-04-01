class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sets = set(nums)
        res = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                #print(i , j)
                val = nums[i] + nums[j]
                #print(val)
                #print(nums[j+1:len(nums)])
                if -val in nums[j+1:len(nums)]:
                    tempt_list= [nums[i],nums[j],-val]
                    tempt_list.sort()
                    #print(tempt_list)
                    if tempt_list not in res:
                        res.append(tempt_list)
        
        return res    
