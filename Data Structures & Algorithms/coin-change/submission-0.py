class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(a):
            if a == 0:
                return 0
            
            if a < 0:
                return float("inf")
            
            if a in memo:
                return memo[a]

            res = float("inf") 

            for coin in coins:
                res = min(res, 1 + dfs(a - coin))

            memo[a] = res
            return memo[a]
        ans = dfs(amount)

        return ans if ans != float("inf") else -1
