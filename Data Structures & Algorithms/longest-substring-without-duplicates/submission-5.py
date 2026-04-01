class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        if len(s)==1:
            return 1
        for i in range(len(s)-1):
            for j in range(i+1,len(s)+1):
                #print(s[i:j],list(set(s[i:j])))
                if len(list(set(s[i:j]))) == len(s[i:j]):
                    res = max(res,len(s[i:j])) 
        return res