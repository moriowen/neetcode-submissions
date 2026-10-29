class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, subset = [], []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        def dfs(i):
            if i == len(digits):
                res.append("".join(subset))
                return 

            for ch in mapping[digits[i]]:
                subset.append(ch)
                dfs(i+1)
                subset.pop()

        dfs(0)
        return res