from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        # write your code here

        slow, fast = 0, 0
        n = len(nums)
        result = []
        temp_sum = 0
        for slow in range(n):

            while fast < n and fast - slow < k:
                temp_sum += nums[fast]
                fast += 1
                # print("fast", fast)
            print(slow, fast)
            if fast - slow == k:
                result.append(temp_sum)
            print("temp_sum", temp_sum)
            temp_sum -= nums[slow]

        return result
# update function with same direction two pointers tempplate
