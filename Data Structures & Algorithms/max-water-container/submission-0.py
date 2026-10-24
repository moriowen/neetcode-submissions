class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        - get bars that are farthest apart - > start from ends for max area
        - take min of the two bars for height to calculate area
        - return area, not index -> keep a max variable 
        - for O(n) only move the smaller of high and low pointers
        """
        max_area = -1
        n = len(heights)
        low, high = 0, n-1

        while low <= high:
            current_area = (high-low) * min(heights[low], heights[high])
            if current_area > max_area:
                max_area = current_area
            
            if heights[low] > heights[high]:
                high -= 1
            else: 
                low +=1 

        return max_area