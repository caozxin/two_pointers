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

        slow, fast = 0, 1
        n = len(nums)
        result = []

        for slow in range(n):

            fast = slow + k
            # print(nums[slow: fast])
            temp_sum = sum(nums[slow: fast])
            # print("temp_sum", temp_sum)
            result.append(temp_sum)

            if fast >= n:
                break

        return result
