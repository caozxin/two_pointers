from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        number_one_idx = ()
        number_two_idx = ()
        # print(number_one, number_two)
        n = len(numbers)
        # numbers.sort() --> you cannot sort it since we need to return the original idx for both
        print(numbers)
        result_list = []

        for idx, value in enumerate(numbers):
            print(idx, value)
            # if target -  value >= 0: 
            if len(result_list) <= 0 :
                number_one_idx = (idx, value)
                remaining_num = target - value
                if remaining_num in numbers:
                    continue
                else:
                    number_one, number_two = (), ()
            elif value == remaining_num :
                number_two_idx = (idx, value) 
                result_list.append(number_one_idx)
                result_list.append(number_two_idx)
                print(result_list)
            else:
                number_one, number_two = float(), float()
        
        if len(result_list) == 2:
            print("result_list", result_list)
            print([result_list[0][0], result_list[1][0]])
            return [result_list[0][0], result_list[1][0]]
        
    def two_sum02(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        number_one_idx = ()
        number_two_idx = ()
        # print(number_one, number_two)
        n = len(numbers)
        # numbers.sort() --> you cannot sort it since we need to return the original idx for both
        print(numbers)
        result_list = []

        for i in range (n):
            
            number_one_idx = (i, numbers[i])
            print(number_one_idx)
            j = i + 1
            while j < n:
                print(i, j)
                if numbers[j] == target - number_one_idx[1]:
                    print("find num2")
                    print("number_one_idx", number_one_idx)
                    number_two_idx = (j, numbers[j])
                    print("number_two_idx", number_two_idx)
                    result_list.append(number_one_idx[0])
                    result_list.append(number_two_idx[0])
                    print("result_list", result_list)
                    return result_list
                
                else:
                    j += 1
            number_one_idx = ()
            j = 0

        print("result_list", result_list)

    def two_sum_with_twopointers(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        if n <= 0:
            return []
        
        nums = []
        for idx, num in enumerate(numbers) :
            nums.append((num, idx))

        nums.sort()
        print("nums", nums)
        result_list = []

        for left in range(n):
            print("I am here")
            for right in range(n -1, -1, -1):
                print(left, right)
                if nums[left] == nums[right]:
                    break
                # print("nums[left], nums[right]")
                # print(nums[left], nums[right])

                if nums[left][0]+ nums[right][0] == target:
                    result_list.append(nums[left][1])
                    result_list.append(nums[right][1])
                    # return [nums[left][0],nums[right][0]]
                    result_list.sort()
                    print("result_list", result_list)
                    return result_list


numbers01 = [2,7,11,15]
target01 = 9


new_solution = Solution()
numbers = [1,3,-1]
target = 2


#update 10/04/2025:
# my not working version:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #none handling:
        if not nums:
            return []
        #note: because nums is not sorted, we need to loop into each num
        right = 1

        for left in range(len(nums)):

            curr_sum = nums[left] + nums[right]
            print(left, right, curr_sum)
            if curr_sum == target:
                    break
            while right > left and right < len(nums) - 1:
                right += 1
                print('right', right)

        return [left, right]

new_solution.two_sum_with_twopointers(numbers01, target01)


#my improved version:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #none handling:
        if not nums:
            return []
        #note: because nums is not sorted, we need to loop into each num

        for left in range(len(nums)):
            right = left + 1

            while right > left and right <= len(nums) - 1:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    return [left, right]
                right += 1

        return []
