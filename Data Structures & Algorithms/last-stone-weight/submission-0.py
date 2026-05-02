class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            #print(abs(y-x))
            if abs(y-x) != 0:
                heapq.heappush(stones,-abs(y-x))
        if stones:
            return -stones[0]
        else:
            return 0
            