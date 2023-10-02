from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer

    description:
    Given an array of integers, find how many pairs in the array 
    such that their sum is less than or equal to a specific target number. Please return the number of pairs.
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        n = len(nums)
        if n <= 0:
            return 0

        nums.sort() # you always want to sort it for two sum type of question.
        print("nums", nums)
        
        result_list = []
        left, right = 0 , n-1

        while left <= right:
            if nums[left] + nums[right] <= target:
                result_list.append((nums[left], nums[right]))
                right -= 1
            elif nums[left] + nums[right] > target:
                left +=1 
                right = n - 1

            if left == right:
                left +=1 
                right = n - 1

                
        print("result_list", result_list, len(result_list))
        return len(result_list)


    def two_sum5_updated(self, nums: List[int], target: int) -> int:        # write your code here
        if not nums:
            return 0

        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum <= target:
                count += right - left  # All pairs between left and right are valid. this is what made this def has less run time. 
                left += 1
            else:
                right -= 1

        return count
numbers01 = [2,7,11,15]
target01 = 24  # return 5 


new_solution = Solution()
numbers = [1]
target = 1
result = new_solution.two_sum5(numbers, target = 1)

print("result", result)