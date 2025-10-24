from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        prefix_prod = [1] * (n + 1)
        suffix_prod = [1] * (n + 1)

        # Build prefix product
        for i in range(n):
            prefix_prod[i + 1] = prefix_prod[i] * nums[i]
            # print(f"Prefix[{i+1}] = {prefix_prod[i+1]} (prefix {prefix_prod[i]} * {nums[i]})")

        # Build suffix product
        for i in range(n - 1, -1, -1):
            suffix_prod[i] = suffix_prod[i + 1] * nums[i]
            # print(f"Suffix[{i}] = {suffix_prod[i]} (suffix {suffix_prod[i+1]} * {nums[i]})")

        # print("Prefix:", prefix_prod)
        # print("Suffix:", suffix_prod)

        # Build result
        result = []
        for i in range(n):
            result.append(prefix_prod[i] * suffix_prod[i + 1])

        return result


# # Example:
# nums = [1, 2, 3, 4]
# print("Result:", Solution().productExceptSelf(nums))
