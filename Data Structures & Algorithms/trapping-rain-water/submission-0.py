class Solution:
    """
    - you need a depression for water to be collected
    - amount of water trapped is min(L, R) - h[i]
    - 
    """
    def trap(self, height: List[int]) -> int:
        low, high = 0, len(height)-1
        max_low, max_high = height[low], height[high]
        trapped_water = 0

        while low < high:
            if max_low < max_high:
                low += 1
                max_low = max(height[low], max_low)
                trapped_water += max_low - height[low]
            else: 
                high -= 1
                max_high = max(height[high], max_high)
                trapped_water += max_high - height[high]
        return trapped_water