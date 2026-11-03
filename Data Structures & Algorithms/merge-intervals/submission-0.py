class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        n = len(intervals)
        res = []

        for i in range(n):
            if not res:
                res.append(intervals[i])
                continue
            
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else: 
                res.append(intervals[i])

        return res