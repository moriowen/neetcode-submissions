from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # Max heap using negative frequencies
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        # (remaining_count, available_time)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            # Execute most frequent available task
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1  # Negative count moves toward 0

                if count < 0:
                    q.append((count, time + n))

            # Move task back to heap after cooldown
            if q and q[0][1] <= time:
                count, _ = q.popleft()
                heapq.heappush(maxHeap, count)

        return time