class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #none handling:
        if not nums:
            return None

        fast, slow = 0, 0
        n = len(nums)

        for fast in range(n):

            if nums[fast] != 0:
                nums[slow], nums[fast]  = nums[fast], nums[slow]
                slow += 1
            print(fast, slow)
