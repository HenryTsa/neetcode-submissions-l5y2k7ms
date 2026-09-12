class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        mid = int(len(self.arr)/2)
        # even
        if len(self.arr)%2 == 0:
            return (self.arr[mid] + self.arr[mid-1])/2
        else:
            return self.arr[mid]

        