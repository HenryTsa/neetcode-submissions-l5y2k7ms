class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # how to use min heap 
        # (wait n ,time , value)
        # each cycle ( wait n - 1 ) O(n)
        counter = Counter(tasks)
        heap = [-c for c in counter.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                cur = heapq.heappop(heap)
                cur += 1
                if cur != 0:
                    queue.append([time+n,cur])
            if queue:
                if time == queue[0][0]:
                    tmp = queue.popleft()
                    heapq.heappush(heap,tmp[1])


        return time
