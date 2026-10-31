class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, 0)]
        visited = set()
        totalCost = 0

        while len(visited) < len(points):
            cost, node = heapq.heappop(minHeap)

            if node in visited:
                continue 

            visited.add(node)
            totalCost += cost

            x1, y1 = points[node]

            for nei in range(len(points)):
                if nei not in visited:
                    x2, y2 = points[nei]
                    dist = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(minHeap, (dist, nei))
        
        return totalCost