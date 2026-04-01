class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap , (-nums[i],i))
        #print(max_heap)
        for i in range(k,len(nums)):
            #print(max_heap)
            res.append(- max_heap[0][0])
            heapq.heappush(max_heap , (-nums[i],i))
            while - max_heap[0][0] == nums[i-k] and max_heap[0][1] <= i-k:
                #print(max_heap)
                heapq.heappop(max_heap)

        res.append(- max_heap[0][0])
        return res