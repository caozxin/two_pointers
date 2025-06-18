from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right] # if nums[right] != nums[left], we make nums[left] = unique nums[right] --> in place manipulation. 
            # print(left, right, nums)
        # Optional: print the updated list for debugging
        # print("Final list (unique values at front):", nums[:left + 1])

        nums = nums[:left + 1]
        return left + 1
