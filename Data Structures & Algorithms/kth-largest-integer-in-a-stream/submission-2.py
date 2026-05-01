class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        lenth = len(nums)-1
        self.heap = []
        for i in range(k):
            if lenth-i >= 0:
                self.heap.append(nums[lenth-i])
        
        # min heap    
        heapq.heapify(self.heap)
        #print(self.heap)
    def add(self, val: int) -> int:
        if self.k > len(self.heap):
            heapq.heappush(self.heap,val)
            return self.heap[0]  
        temp_smallest = heapq.heappop(self.heap)
        if val > temp_smallest:
            heapq.heappush(self.heap,val)
        else:
            heapq.heappush(self.heap,temp_smallest)
        return self.heap[0]  
        
