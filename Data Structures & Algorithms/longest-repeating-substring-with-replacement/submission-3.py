class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        # 從 i 開始 j 跑過從 i 開始最大的
        for i in range(len(s)):
            count = {}
            maxf = 0
            for j in range(i,len(s)):
                # 每經過一次 s[j] 這個值累計一次,然後看哪個值出現在多次
                count[s[j]] = 1+ count.get(s[j],0)
                maxf = max(maxf,count[s[j]])
                if (j-i+1) - maxf <= k:
                    res = max(res,j-i+1)
        return res 