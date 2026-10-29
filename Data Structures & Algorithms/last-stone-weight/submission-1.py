class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)

            diff = abs(stone2 - stone1)
            heapq.heappush(maxHeap, -diff)
        
        return -maxHeap[0]