class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        - Use a monotonically decreasing stack of indices
        - For each temperature, pop while current > stack top
        - Calculate days waited using index difference
        - Push current index
        - Unresolved days remain 0
        """
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        
        return res

