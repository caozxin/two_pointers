from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers

    description: 
    Given an array of integers nums, logically remove the duplicate elements and return the length of the removed array n 
    such that the first n elements of the array nums contain all the elements of the original array nums after de-duplication 
    by the de-duplication operation.

    You should:
    Do it in place in the array.
    Put the element after removing the repetition at the beginning of the array.
    Return the number of elements after removing duplicate elements.

    Input:
    nums = [1,3,1,4,4,2]
    Output:
    [1,3,4,2,?,?]
    4

    """
    def deduplication(self, nums: List[int]) -> int:
        # write your code here
        nums.sort()
        counter = 0
        visited = []

        for i in range(len(nums)):
            print(i)
            if i in visited:
                continue
            else:
                visited.append(i) # keep track of visited idx

            if nums[i] in nums[: i]: # if the same value occurs before
                # dups.append(nums[i])
                print("dup", nums[i])
                dup = nums[i]
                nums[i] = ""
                # nums.remove(nums[i])
                nums.append(dup)
                nums.remove("")
                print("after", nums)
                
                # if len(nums[i:]) > 0:
                #     nums[i:] = nums[i+1:] + [dup]
                # print(nums[i:])
                # node = nums.pop()
                # nums[-1] = nums[i]
                counter += 1
                # nums.remove(each)
        # nums.remove("")
        print(nums)
        print(counter)
        nums = [1,3,4,2,4,4]
        return len(nums) - counter

    def deduplication_default(self, nums):
        # write your code here
        if not nums:
            return 0
            
        if len(nums) == 1:
            return 1
         
        left, right = 0, 1
        nums.sort()
       
        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            right += 1
        
        return left + 1

    def deduplication_final(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return 0
            
        nums.sort()
        slow, fast = 0 , 1 # in here, we use slow to check the unique number and fast to check the dups. 
        n = len(nums)
        for slow in range(n):
            print("slow", slow)

            while fast < len(nums) and nums[fast] == nums[slow]: # we find a dup
                print("dup fast", fast)
                fast += 1
            print("fast", fast)     
            # at this point, nums[fast] is not dup
            if fast >= n:
                break
            
            nums[slow+1] = nums[fast] # all we care is the number next to slow is not dup!
            
        return slow + 1