class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force: examine every subarray and track the maximum sum
        # A decrease in the running sum doesn't necessarily mean we should reset
        # At each index, decide whether to extend the previous subarray or start fresh
        # Keep track of the maximum sum ending at the current index
        # Update the global maximum after processing each element

        max_sa = float("-inf")
        total = 0

        for num in nums:
            total += num
            max_sa = max(max_sa, total)

            if total < 0:
                total = 0
            
        return max_sa

            
            