class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0

        for num in range(len(nums)):
            if num > reach:
                return False
            reach = max(reach, num + nums[num])
        
        return reach >= len(nums)-1