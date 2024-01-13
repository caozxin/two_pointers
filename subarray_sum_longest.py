# Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the longest subarray that does not exceed 10 is [3, 1, 2, 4], so the output is 4 (length of [3, 1, 2, 4]).

from typing import List

def subarray_sum_longest(nums: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
#     print("input", nums, target)
    if not nums: 
        return 0
    n = len(nums)
    left, right = 0, 0
    curr_sum = 0
    max_len = 0 
    
    for right in range(n):
        curr_sum += nums[right]
        window = nums[left: right+1]
#         print("*curr_sum", curr_sum)
        curr_len = right - left + 1
#         print("*window", window)
#         print("*curr_len", curr_len)
        
        if curr_sum > target:
            left += 1
            curr_sum -= nums[left]
        else:
            max_len = max(max_len, curr_len)
            right += 1
#         print("window", window)
#         window = nums[left: right+1]
        
#         print('curr_len', left, right, curr_len)
#         print("    window", window)
        
#         print('    max_len', max_len)
    return max_len
