class Solution:
    def longestConsecutive(self, nums):
        if len(nums)<1:
            return 0
        arr = sorted(nums)
        # arr = set(nums)
        # arr = list(arr)
        max_len = 1 
        cur_len = 1
        print(arr)
        for i,number in enumerate(arr):
            if i!=0 and number == arr[i-1]:
                continue
            elif i!=0 and number == arr[i-1]+1:
                cur_len += 1
            else:
                cur_len = 1
            max_len = max(max_len,cur_len)

        return max_len