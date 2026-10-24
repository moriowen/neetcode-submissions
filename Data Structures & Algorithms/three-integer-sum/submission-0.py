class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            
            low, high = index+1, len(nums)-1
            
            while low < high:
                if nums[low] + nums[high] > -1 * num:
                    high -= 1
                elif nums[low] + nums[high] < -1 * num:
                    low += 1
                else: 
                    res.append([num, nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low-1]:
                        low += 1


        return res