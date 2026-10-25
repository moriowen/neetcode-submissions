class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        - monotonic stack (decreasing)
        - push into the stack until a larger element is found, then pop everything 
        - populate the values using the index of this new larger element
        """
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][1] > temp:
                stack.append((i, temp))
            else: 
                while stack and stack[-1][1] < temp:
                    top_temp = stack.pop()
                    res[top_temp[0]] = i - top_temp[0]
                stack.append((i, temp))
        
        return res

