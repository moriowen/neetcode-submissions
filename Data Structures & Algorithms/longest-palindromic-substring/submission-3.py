class Solution:
    def longestPalindrome(self, s: str) -> str:
        # rather than looping over the entire str, start on each index and expand outwards as long as its a palindrome
        # approach differs for even and odd index

        n = len(s)
        res = ""

        for i in range(n):
            for l, r in [(i, i+1), (i, i)]:
                while l >= 0 and r < n and s[l] == s[r]: 
                    if len(res) < len(s[l:r+1]):
                        res = s[l:r+1]
                    l -= 1
                    r += 1

        return res