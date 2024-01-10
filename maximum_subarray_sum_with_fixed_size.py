#Given an array (list) nums consisted of only non-negative integers, find the largest sum among all subarrays of length k in nums.

#For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by [3, 7, 4] which sums to 14.

#https://algo.monster/problems/subarray_sum_fixed

from typing import List

def subarray_sum_fixed(nums: List[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if not nums:
        return 0
    
    #initianize the window
    window = nums[:k]
    n = len(nums)
#     print(n, len(window))
    
    max_sum = sum(window)# this is the only time you will use sum()!
#     print("max_sum", max_sum)
    
    for right in range(k, n+1): # k step, total n+1 (b/c right endpoint needs to be 1 size bigger for slicing)
#         print(right)
        left = right - k
#         print(left, right, nums[left:right])
        window = nums[left:right] # keep using the slicing to make it consistent
        curr_sum = max_sum - window[0] + window[-1]
#         print("curr_sum", curr_sum, window[0], window[-1])
        if curr_sum > max_sum:
            max_sum = curr_sum
            
    return max_sum
