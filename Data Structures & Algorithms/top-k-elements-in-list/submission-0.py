class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 0
            else: 
                d[num] += 1
        
        sorted_nums = sorted(d.items(), key= lambda x:x[1], reverse=True)

        return [sorted_nums[x][0] for x in range(k)]