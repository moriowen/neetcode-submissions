class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_index = self.find_pivot(nums)

        def binary_search(low, high):
            while low <= high:
                mid = (low+high) // 2

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    return mid
            return -1

        # if right half 
        res_left = binary_search(pivot_index, len(nums)-1)
        if res_left != -1:
            return res_left
        else: 
            return binary_search(0, pivot_index-1)

    def find_pivot(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else: 
                r = mid
            
        return l


