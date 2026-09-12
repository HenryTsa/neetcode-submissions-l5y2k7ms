class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        
        # 插入數量比較少的 來調整
        # judge min or max
        # max: [ 1 ]         min: [ 3 ]           
        # 打算插入 max 新的      
        #print("min",self.minheap)
        #print("max",self.maxheap)
        if len(self.maxheap) <= len(self.minheap):
            if len(self.maxheap) == 0:
                heapq.heappush(self.maxheap,-num)
                return
            mix_value = -self.maxheap[0]
            max_value = self.minheap[0]
            if max_value < num:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap,num)
                heapq.heappush(self.maxheap,-max_value)
            else:
                heapq.heappush(self.maxheap,-num)
        # 打算插入 min 新的
        else:
            min_value = -self.maxheap[0]
            if len(self.minheap) == 0:
                if num < min_value:
                    heapq.heappop(self.maxheap)
                    heapq.heappush(self.maxheap,-num)
                    heapq.heappush(self.minheap,min_value)
                else:
                    heapq.heappush(self.minheap,num)
                return
            
            max_value = self.minheap[0]
            if max_value > num:
                heapq.heappop(self.maxheap)
                heapq.heappush(self.maxheap,-num)
                heapq.heappush(self.minheap,min_value)
            else:
                heapq.heappush(self.minheap,num)
        #print("new_min",self.minheap)
        #print("new_max",self.maxheap)
        

    def findMedian(self) -> float:

        # even
        if (len(self.minheap)+len(self.maxheap))%2 == 0:
            return (self.minheap[0] + -self.maxheap[0])/2
        else:
            return -self.maxheap[0]

        