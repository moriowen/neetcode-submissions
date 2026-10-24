class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs: 
            sorted_str = ''.join(sorted(s))
            if sorted_str in d: 
                d[sorted_str].append(s)
            else: 
                d[sorted_str] = [s]
        
        return list(d.values())
