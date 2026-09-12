class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        
        # 插入數量比較少的 來調整
        # judge min or max
        # max: [ 1 ]         min: [ 3 ]    
              
        # 打算插入 max 新的      
        heapq.heappush(self.maxheap,-num)
        
        if len(self.maxheap) > len(self.minheap)+1:
            value = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,value)
        if len(self.minheap)==0:
            return
        if self.minheap[0] < -self.maxheap[0]:
            min_value = -heapq.heappop(self.maxheap)
            max_value = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-max_value)
            heapq.heappush(self.minheap,min_value)

        
        

    def findMedian(self) -> float:
        # print("new_min",self.minheap)
        # print("new_max",self.maxheap) 
        # even
        if (len(self.minheap)+len(self.maxheap))%2 == 0:
            return (self.minheap[0] + -self.maxheap[0])/2
        else:
            return -self.maxheap[0]

        