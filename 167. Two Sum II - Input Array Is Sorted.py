class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # none handling:
        if not numbers:
            return [] # return format needs to be consistent

        n = len(numbers)
        left, right = 0, n-1 # final return should be [left+1, right+1]

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: 
                left += 1

        return [] # return format needs to be consistent
