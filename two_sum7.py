from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)

    description: Given an sorted array of integers, find two numbers that their difference equals to a target value.
    Return a list with two number like [num1, num2] that the difference of num1 and num2 equals to target value, and num1 is less than num2.

        Input: nums = [2, 7, 15, 24], target = 5 
        Output: [2, 7] 
        Explanation:
        (7 - 2 = 5)

        Input: nums = [1, 1], target = 0
        Output: [1, 1] 
        Explanation:
        (1 - 1 = 0)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        # write your code here

        fast, slow = 1, 0
        n = len(nums)
        result = []
        target = abs(target)

        while fast < n and slow <= fast:

            gap = abs(nums[fast] - nums[slow])
            print(nums[slow], nums[fast])

            if gap == target:
                result = [nums[slow], nums[fast]]
                return result
            elif gap < target : # this turning condiction is not accurate enough
                fast += 1
            else:
                slow += 1
                if slow == fast: # this step is needed to avoid when slow == fast
                    fast = slow + 1

        return result
    
    def two_sum702(self, nums: List[int], target: int) -> List[int]:
        # write your code here

        n = len(nums)

        for slow in range(n):
            fast = slow + 1

            while fast < n:
                gap = abs(nums[fast] - nums[slow])

                if gap == target:
                    return [nums[slow], nums[fast]]
                elif gap < target:
                    fast += 1
                else:
                    break  # Stop increasing fast if the gap exceeds the target

        return []  # Return an empty list if no such pair is found

new_solution = Solution()
nums = [2, 7, 15, 24]
target = 5 
nums = [0,1,2,2]
target = 0
nums = [0,5,7]
target = -2

result = new_solution.two_sum7(nums, target)
print("result", result)