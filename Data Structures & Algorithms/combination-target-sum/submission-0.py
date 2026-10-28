class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def dfs(i, total):

            if sum(subset) > target or i == len(nums):
                return 
            
            if sum(subset) == target:
                res.append(subset.copy())
                return 

            # include
            subset.append(nums[i])
            dfs(i, total + nums[i])
        
            # not take
            subset.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res 