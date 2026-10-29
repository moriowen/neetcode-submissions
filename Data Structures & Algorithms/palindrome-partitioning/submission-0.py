class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, subset = [], []

        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return 
            
            for j in range(i+1, len(s)+1):
                part = s[i:j]
                if part == part[::-1]:
                    subset.append(part)
                    dfs(j)
                    subset.pop()

        dfs(0)
        return res