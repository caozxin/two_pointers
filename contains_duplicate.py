#Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

from typing import (
    List,
)

from collections import Counter

class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def contains_duplicate(self, nums: List[int]) -> bool:
        # Write your code here
        x = Counter(nums)

        print(x)

        for each in x.values():
            print(each)
            if each > 1:
                return True
        return False
