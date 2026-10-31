class Solution:
    def rob(self, nums: List[int]) -> int:
        # at each index, we can either take or skipit depending on whether the prev was taken 
        # can we skip two? so we can (n+2) and (n+3)? should we not even go for (n+1) since that will trigger the alarm 
        # steal the max amount of money - take max at each iteration? cost + max(dfs(n+2), dfs(n+3))
        # keep a memo array 

        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            take = nums[i] + dfs(i+2)
            skip = dfs(i+1)

            memo[i] = max(take, skip)
        
            return memo[i]
        
        return dfs(0)