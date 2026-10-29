class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            minHeap.append((dist, point))
        
        heapq.heapify(minHeap)

        res = []

        while k:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1
        
        return res
