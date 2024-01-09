from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def max_sub_array(self, nums: List[int]) -> int: # Kadane's algorithm
        if not nums:
            return 0

        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    def max_sub_array01(self, nums: List[int]) -> int:
        if not nums:
            return 0  # If the list is empty, the sum of the max subarray is 0

        n = len(nums)
        max_sum = float('-inf')
        
        for i in range(1, n + 1):  # Iterate over all possible subarray lengths
            for left in range(n - i + 1):
                right = left + i
                window = nums[left:right]
                current_sum = sum(window)
                
                # Update max_sum if the current subarray sum is greater
                if current_sum > max_sum:
                    max_sum = current_sum
        
        return max_sum

    def max_sub_array00(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return 0 # matches with the expected output format

        n = len(nums)
        left, right = 0 , 1
        max_sum = float('-inf')
        max_sum = sum(nums)

        for i in range(n):
            print(i)
            left = 0 
            
            while left < n and left <= right:
                right = left + i
                window = nums[left:right]
                if len(window) == i:
                    if sum(window) > max_sum:
                        max_sum = sum(window)
                
                left += 1
        return max_sum
