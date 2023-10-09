from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer

    description: Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

    Input: nums = [1,1,2,45,46,46], target = 47 
    Output: 2
    Explanation:
    1 + 46 = 47
    2 + 45 = 47

    Input: nums = [1,1], target = 2 
    Output: 1
    Explanation:
    1 + 1 = 2
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        # make the nums into unique set()
        
        nums_set = set()

        for each in nums:
            nums_set.add(each)

        n = len(nums_set)
        # print("nums_set", nums_set)
        # print("nums_set", list(nums_set)[0])

        if n == 1 and len(nums) > 1 and target % list(nums_set)[0] == 0 : # this is handle only one duplicate case
            return 1
        
        counter = 0
        unique_list = list(nums_set)
        unique_list.sort()

        if len(unique_list) <= 1:
            return 0

        left, right = 0 , n-1

        while left <= right:
            if unique_list[left] + unique_list[right] == target:
                counter += 1

            if unique_list[left] + unique_list[right] <= target and left < right :
                left += 1
            
            if unique_list[left] + unique_list[right] >= target and left < right:
                right -= 1
            
            if left == right:
                break
        
        return counter
    def two_sum6_02(self, nums: List[int], target: int) -> int:
        # write your code here
        # make the nums into unique set()
        
        n = len(nums)
        nums.sort()

        if n <= 1:
            return 0
        
        pair_list = set()
        counter = 0
        left, right = 0 , n-1

        while left <= right:
            if nums[left] + nums[right] == target:
                curr_pair = (nums[left] , nums[right])
                if curr_pair not in pair_list:
                    pair_list.add(curr_pair)
                    counter += 1

            if nums[left] + nums[right] <= target and left < right :
                left += 1
            
            elif nums[left] + nums[right] >= target and left < right:
                right -= 1
            
            if left == right:
                break
        
        return counter
new_solution = Solution()

nums = [1,1,2,45,46,46]
target = 47 
nums02= [ 1, 1, 1, 1]
target02 = 2 
nums03 = [7,11,11,1,2,3,4]
target03 = 22
nums05 = [1,0,-1]
target05 = 0

result = new_solution.two_sum6_02(nums, target)
print("result", result)