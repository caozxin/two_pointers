# Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the longest subarray that does not exceed 10 is [3, 1, 2, 4], so the output is 4 (length of [3, 1, 2, 4]).

from typing import List

def subarray_sum_longest(nums: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    print("input", nums, target)
    if not nums: 
        return 0
    n = len(nums)
    k = 1 # k = length of the substring
    max_length = 0 
    window = nums[:k]
    curr_sum = sum(window)
    left, right = 0, 0
    while right < n and left <= right: 
        
        window = nums[left:right+1]
        print(left, right, window)
        
        #             curr_sum = curr_sum - window[0] + window[-1] # curr_sum did not get update properly
        curr_sum -= nums[left]
        curr_sum += nums[right]
        print("    curr_sum", curr_sum)
        print("    window_sum", sum(window))
        
        if curr_sum <= target:
            right += 1 # left and right are the same direction, you update right when curr_sum < target; otherwise update left.
            
        else:
            exit()
            left += 1 
        max_length = max(max_length, len(window))
        print("max_length", max_length)
