from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def max_sub_array(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return None
        nums.sort()
        nums.reverse()
        print(nums)
        n = len(nums)
        left, right = 0 , 1
        # max_sum = float('-inf')
        max_sum = sum(nums)

        for i in range(n):
            print(i)
            left = 0 

            while left < n and left <= right:
                right = left + i
                window = nums[left:right]
                if len(window) == i:
                    print("window", window, left, right)
                    if sum(window) > max_sum:
                        max_sum = sum(window)
                
                left += 1
        return max_sum

    def max_sub_array00(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return None
        nums.sort()
        nums.reverse()
        print(nums)
        n = len(nums)
        left, right = 0 , 1
        # max_sum = float('-inf')
        max_sum = sum(nums)

        for i in range(n):
            print(i)
            left = 0 

            while left < n and left <= right:
                right = left + i
                window = nums[left:right]
                if len(window) == i:
                    print("window", window, left, right)
                    if sum(window) > max_sum:
                        max_sum = sum(window)
                
                left += 1
        return max_sum
