class Solution:
    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s)-1
        
        while low < high: 
            while low < high and not self.isAlphaNum(s[low]):
                low += 1
            while low < high and not self.isAlphaNum(s[high]):
                high -= 1

            if s[low].lower() != s[high].lower():
                return False
            
            low += 1
            high -= 1
        
        return True

    def isAlphaNum(self, num):
        if 65 <= ord(num) <= 90 or 97 <= ord(num) <= 122 or ord('0') <= ord(num) <= ord('9'):
            return True