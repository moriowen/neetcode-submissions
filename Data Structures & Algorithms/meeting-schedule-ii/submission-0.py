"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # keep a min heap to store end times
        # if min top of min heap < current, an older meeting is still in progress
        # increment the count of rooms 
        intervals.sort(key=lambda x: x.start)
        minHeap = []

        for i in intervals:
            start, end = i.start, i.end
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, end)
        
        return len(minHeap)