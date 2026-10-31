class Solution:
    def rob(self, nums: List[int]) -> int:
        # Houses form a circle, so the first and last cannot both be robbed
        # Split into two cases: exclude the first house or exclude the last
        # For each case, either rob the current house or skip it
        # If robbed, continue from i+2; if skipped, continue from i+1
        # Memoize overlapping subproblems and return the maximum of both case
        
        if len(nums) == 1:
            return nums[0]

        def dfs(i, arr, memo):
            if i >= len(arr):
                return 0

            if i in memo:
                return memo[i]
            
            take = arr[i] + dfs(i+2, arr, memo)
            skip = dfs(i+1, arr, memo)

            memo[i] = max(take, skip)
            return memo[i]

        
        excluding_first = dfs(0, nums[1:], {})
        excluding_last = dfs(0, nums[:-1], {})

        return max(excluding_first, excluding_last)
        
        