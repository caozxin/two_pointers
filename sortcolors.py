class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return None
        
        start, curr, end = -1, 0, len(nums) 

        while curr < end:
            print("curr_nums: ", nums)
            print(curr, start, end)
            if nums[curr] == 0: # move it to left
                start += 1
                nums[start], nums[curr] = 0, nums[start]
                
                curr += 1

            elif nums[curr] == 2: # move it to right
                end -= 1
                # exit()
                nums[curr], nums[end] = nums[end], 2
                
            elif nums[curr] == 1:
                curr += 1
        
