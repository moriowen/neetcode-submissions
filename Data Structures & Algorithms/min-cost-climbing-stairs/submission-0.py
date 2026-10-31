class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)

        def dfs(n):
            if n >= len(cost):
                return 0

            if n in memo:
                return memo[n]

            memo[n] = cost[n] + min(dfs(n + 1), dfs(n + 2)) 
            return memo[n]
        
        return min(dfs(0), dfs(1))