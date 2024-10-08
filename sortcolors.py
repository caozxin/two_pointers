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
                # noteNote: When we decrement the end pointer, 
                # the current pointer remains unchanged since it has to analyze the swapped element to determine 
                # if further swapping is required with the start pointer
                nums[curr], nums[end] = nums[end], 2
                
            elif nums[curr] == 1:
                curr += 1
        
