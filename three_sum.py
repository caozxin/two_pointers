from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output

    description: Given an array S of n integers, 
    are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    numbers = [2,7,11,15]
    output = []

    numbers = [-1,0,1,2,-1,-4]
    [[-1, 0, 1],[-1, -1, 2]]

    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        
        n = len(numbers)

        if n < 3:  # --> this is the base case
            return []
        
        # left, right = 0 , n-1
        numbers.sort()
        result_list = list()

        for i in range(n-1, -1, -1):
            pivot = -numbers[i]
            print("pivot", i, pivot, numbers[:i])
            left, right = 0, i - 1

            # if len(numbers[:i]) < 3:
            #     break

            while left <= right:
                if numbers[left] + numbers[right] == pivot and left < right:
                    curr_result = [numbers[left],numbers[right],  -pivot]
                    if curr_result not in result_list:
                        result_list.append(curr_result)
                    right -= 1
                elif numbers[left] + numbers[right] < pivot and left < right:
                    left += 1
                elif numbers[left] + numbers[right] >= pivot and left < right:
                    right -= 1
                
                if left == right:
                    i -= 1
                    
                    break
        
        return result_list

new_solution = Solution()
numbers = [2,7,11,15]
numbers02 = [-1,0,1,2,-1,-4]
numbers03 = [-1,1,0]
result = new_solution.three_sum(numbers03)
print("result", result)