class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        if len(s)==1:
            return 1
        for length in range(1,len(s)+1):
            #print(length)
            for idx in range(0,len(s)-length+1):
                tempt = {}
                #print(idx,length)
                for j in range(length):
                    if s[idx+j] in tempt:
                        break
                    tempt[s[idx + j]] = 1
                #print(tempt)
                res = max(res,len(list(tempt.values())))
            
        return res