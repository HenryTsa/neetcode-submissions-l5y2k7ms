class Solution:
    def judge(self,k,h,piles):
        step = 0
        for pile in piles:
            step += math.ceil(pile/k)
        if step <= h:
            return True
        else:
            return False
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # each pile spent piles[i] / k 
        # piles[0] / k + piles[1] / k ... + piles[n]/k  <= h
        # (pile[0] + ... + piles[n])/h <= k
        l,r = 1,max(piles)
        final_k = r
        while l<=r:
            mid = int((l+r)/2)
            if self.judge(mid,h,piles):
                final_k = mid
                r = mid-1
            else:
                l = mid + 1 
            
        #print(final_k)
        return final_k
