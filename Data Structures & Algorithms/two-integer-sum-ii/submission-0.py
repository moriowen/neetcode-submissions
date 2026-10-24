class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) 
        low, high = 0, n-1

        while low <= high:
            if numbers[low] + numbers[high] > target:
                high -= 1
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                return [low+1, high+1]