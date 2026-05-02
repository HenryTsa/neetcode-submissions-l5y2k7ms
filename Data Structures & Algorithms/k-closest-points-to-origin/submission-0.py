class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        res = []
        for i in range(len(points)):
            dis = points[i][0]**2 + points[i][1]**2
            arr.append([dis, points[i][0], points[i][1]])
        heapq.heapify(arr)
        for i in range(k):
            tmp = heapq.heappop(arr)
            res.append([tmp[1],tmp[2]])
        return res