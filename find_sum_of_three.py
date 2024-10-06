#my version
def find_sum_of_three(nums, target):
   
   # Replace this placeholder return statement with your code

  nums.sort()  # Sort the list
  
  for i in range(len(nums) - 2):
      # Skip duplicate elements
      if i > 0 and nums[i] == nums[i - 1]:
          continue
      
      # If the current number is greater than 0, break early since we can't sum to zero
      if nums[i] > target:
          break
      
      # Two pointers for the rest of the elements
      low, high = i + 1, len(nums) - 1
      while low < high:
          curr_sum = nums[i] + nums[low] + nums[high]
          # print(curr_sum, low, high)
          if curr_sum < target:
              low += 1
          elif curr_sum > target:
              high -= 1
          else:
            return True
  return False

#my improved version:
def find_sum_of_three(nums, target):
   
   # Replace this placeholder return statement with your code

  nums.sort()  # Sort the list
  
  for i in range(len(nums) - 2):
      # Skip duplicate elements
      if i > 0 and nums[i] == nums[i - 1]:
          continue
      
      # Two pointers for the rest of the elements
      low, high = i + 1, len(nums) - 1
      while low < high:
          curr_sum = nums[i] + nums[low] + nums[high]
          # print(curr)
          if curr_sum < target:
              low += 1
          elif curr_sum > target:
              high -= 1
          else:
            return True
  return False
