class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        - binary search over range 
        - time to eat one pile = ceil(pile/rate)
        - total time to eat <= h
        - check for all values from min
        - range - low - atleast 1 and max is max of piles, anything more will just be the same
        """

        low, high = 1, max(piles)
        res = high
        
        while low <= high:
            mid = (low+high)//2

            if self.finish_pile(piles, mid, h):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res


    def finish_pile(self, piles, rate, h):
        return sum([math.ceil(x/rate) for x in piles]) <= h