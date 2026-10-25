class Solution:
    def isValid(self, s: str) -> bool:
        """
        - Use stack + closing-to-opening hashmap
        - Iterate through characters
        - Opening bracket → push to stack
        - Closing bracket → if stack empty or top mismatches, return False
        - Otherwise, pop stack
        - Return True if stack is empty
        """
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0
        