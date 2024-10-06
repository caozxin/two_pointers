#my 1st version:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if the result is  a set()

        res = list()
        #none handeling:
        if not nums or len(nums) < 3:
            return []

        # set the for loop for the first element:
        nums.sort()
        # print(nums)
        for i in range(len(nums)-2): # we only consider in range of 3
            # print(i, nums[i])
            if nums[i] > 0:
                break

            curr_nums = nums[i+1:]
            # print(curr_nums)
            k = len(curr_nums)
            curr_sum = nums[i]

            low, high = 0, k - 1

            while low < high:
                if curr_nums[low]+curr_nums[high] + curr_sum < 0:
                    low += 1
                elif curr_nums[low]+curr_nums[high] + curr_sum > 0:
                    high -= 1
                else:
                    curr_list = [curr_nums[low], curr_nums[high],  curr_sum]
                    if curr_list not in res:
                        res.append(curr_list)
                    low += 1 
                    high -= 1
        # print(res)
        return res
        exit()
# improved version:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the list
        
        for i in range(len(nums) - 2):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # If the current number is greater than 0, break early since we can't sum to zero
            if nums[i] > 0:
                break
            
            # Two pointers for the rest of the elements
            low, high = i + 1, len(nums) - 1
            while low < high:
                curr_sum = nums[i] + nums[low] + nums[high]
                
                if curr_sum < 0:
                    low += 1
                elif curr_sum > 0:
                    high -= 1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    
                    # Skip duplicate elements for low and high
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    
                    # Move the pointers forward
                    low += 1
                    high -= 1
        
        return res


