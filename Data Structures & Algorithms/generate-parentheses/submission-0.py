class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, subset = [], []

        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append("".join(subset))

            if openN < n:
                subset.append("(")
                dfs(openN+1, closeN)
                subset.pop()
            
            if closeN < openN:
                subset.append(")")
                dfs(openN, closeN+1)
                subset.pop()

        dfs(0, 0)
        return res