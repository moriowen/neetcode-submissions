class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        - find the element that has a larger number on either side 
        """
        low, high = 0, len(nums)-1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[high]:
                high = mid 
            else:
                low = mid + 1
        return nums[low]

        