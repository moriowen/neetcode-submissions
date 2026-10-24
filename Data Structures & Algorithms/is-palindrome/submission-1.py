class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ""
        for st in s:
            if st.isalnum():
                cleaned_str += st.lower()

        return cleaned_str == cleaned_str[::-1]