class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # how to use min heap 
        # (wait n ,time , value)
        # each cycle ( wait n - 1 ) O(n)
        dic = defaultdict(int)
        arr = []
        res = 0
        for i in range(len(tasks)):
            if tasks[i] not in dic:
                dic[tasks[i]] = 1
            else:
                dic[tasks[i]] += 1
        for i in dic.keys():
            arr.append([0,-dic[i],i])
        #print(arr)
        heapq.heapify(arr)
        while arr:
            res += 1
            #print(arr)
            cur = heapq.heappop(arr)
            #print(cur)
            if cur[0] == 0:
                cur[1] +=1
                cur[0] = n+1
                if cur[1] != 0:
                    heapq.heappush(arr,cur)
            else:
                heapq.heappush(arr,cur)
            for cur in arr:
                cur[0] = cur[0]-1 if cur[0]!=0 else 0
            heapq.heapify(arr)


        return res
        