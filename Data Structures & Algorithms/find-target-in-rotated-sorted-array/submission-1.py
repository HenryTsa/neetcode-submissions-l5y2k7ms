class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        # 我先找到 peak，然後判斷在左邊還是右邊
        mid = 0
        skip = 0
        if nums[l] <= nums[r]:
            mid = r
            skip = 1
        #print()
        while l <= r :
            if skip == 1:
                break
            mid = (l+r)//2
            #print(mid,l,r)
            if mid!= len(nums)-1 and nums[mid] > nums[mid+1] :
                break
            # 在左邊斜坡
            if nums[mid] > nums[l]: 
                l = mid + 1 
            # 在右邊斜坡    
            elif nums[mid] < nums[l] :
                r = mid -  1
        #print("largest",mid)
        if target < nums[0]:
            l = mid + 1
            r = len(nums)-1
        else:
            l = 0
            r = mid
        
        while l<=r:
            mid = (l+r)//2
            #print(l,r,mid)
            if nums[mid] == target:
                return mid
            elif nums[mid]> target:
                r = mid -1
            else:
                l = mid +1  
        
        return -1