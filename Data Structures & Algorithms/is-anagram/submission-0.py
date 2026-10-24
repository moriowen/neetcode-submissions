class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s, counter_t = {}, {}

        for i in s: 
            if i in counter_s: 
                counter_s[i] += 1
            else: 
                counter_s[i] = 1
        for i in t: 
            if i in counter_t: 
                counter_t[i] += 1
            else: 
                counter_t[i] = 1
        return counter_s == counter_t