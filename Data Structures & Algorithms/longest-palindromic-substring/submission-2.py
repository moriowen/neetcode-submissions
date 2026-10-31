class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi = [0, ""]

        for i in range(len(s)):
            for j in range(i, len(s)):
                st = s[i:j+1]

                if st == st[::-1]:
                    if maxi[0] < len(st):
                        maxi = [len(st), st]

        return maxi[1]
