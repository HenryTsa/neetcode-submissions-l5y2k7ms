class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        unique_number = set()
        l,r =0,0
        if len(s)==0:
            return 0
        unique_number.add(s[l])
        while r < len(s)-1:
            #print(unique_number,l,r,res)
            r += 1
            #print(unique_number,s[r],res,l,r)
            if s[r] not in unique_number:
                unique_number.add(s[r])
                res = max(res,r-l+1)
                #print(res)
            else:
                print(l,r,unique_number)
                #print(s[l:r+1],unique_number)
                while s[l] != s[r] and l<r:
                    unique_number.discard(s[l])
                    l += 1
                l += 1 
                #print(l,r,unique_number)
        return res