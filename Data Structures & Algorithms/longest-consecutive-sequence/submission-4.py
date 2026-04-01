class Solution:
    def longestConsecutive(self, nums):
        sets = set(nums)
        res = 0
        for number in sets:
            cur_len = 1
            if number - 1 not in sets:
                while number + cur_len in sets:
                    print(number + cur_len)
                    cur_len += 1
            print()
            res = max(res,cur_len) 
        return res