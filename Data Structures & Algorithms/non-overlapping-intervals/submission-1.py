class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by end time to maximize available space.
        # Always keep the interval that finishes earliest.
        # Select the first interval and initialize count to 1.
        # Keep another interval only if its start >= last selected end.
        # Minimum removals = total intervals - maximum non-overlapping intervals.

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        last_end_time = intervals[0][1]
        meeting_count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= last_end_time:
                meeting_count += 1
                last_end_time = intervals[i][1]

        return len(intervals) - meeting_count