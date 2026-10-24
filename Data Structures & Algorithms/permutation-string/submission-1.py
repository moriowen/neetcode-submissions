class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        - Fixed window of len(s1); compare char frequencies
        - Build freq1 once; maintain freq2 for s2 window
        - Expand R: add s2[R] to freq2
        - If window > len(s1): remove s2[L], move L
        - If freq1 == freq2: return True
        """

        l = 0
        s1_freq, s2_freq = {}, {}

        for st in s1:
            s1_freq[st] = 1 + s1_freq.get(st, 0)

        for r in range(len(s2)):
            s2_freq[s2[r]] = 1 + s2_freq.get(s2[r], 0)

            window = r - l + 1
            if window > len(s1): # update window 
                s2_freq[s2[l]] -= 1

                if s2_freq[s2[l]] == 0:
                    del s2_freq[s2[l]]
                l += 1

            if s1_freq == s2_freq:
                return True
    
        return False
