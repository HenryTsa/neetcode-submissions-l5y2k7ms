class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 目標找到斜坡 l < r 代表說已經 rotate 過了，如果 l > r  min = len
        # 已經先處理掉了，現在來看兩個斜坡的，試試看找最大的，然後 +1 
        l,r = 0,len(nums)-1
        if nums[l]<=nums[r]:
            return nums[l]
        while l<=r:
            mid = (l+r)//2
            #print(mid,nums[mid],l,r)
            # 找到最高點了
            if mid!= len(nums)-1 and nums[mid] > nums[mid+1] :
                return nums[mid+1]
            elif nums[mid]<nums[l]:
                r = mid - 1
            else:
                l = mid + 1

        return 0