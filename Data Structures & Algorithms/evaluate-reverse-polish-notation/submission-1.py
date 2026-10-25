class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        - push into a stack
        - pop twice when you find an operator
        - calculate and push to stack again 
        """
        st = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                st.append(int(token))
            else: 
                a = st.pop()
                b = st.pop()
                res = 0

                if token == "+":
                    res = b + a
                elif token == "-":
                    res = b - a
                elif token == "*":
                    res = b * a
                elif token == "/":
                    res = int(b / a)
                
                st.append(res)

        return st[-1]