from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer

    description: Given an positive integer array A and an interval. Return the number of subarrays whose sum is in the range of given interval.

    Input: A = [1, 2, 3, 4], start = 1, end = 3
    Output: 4
    Explanation: All possible subarrays: [1](sum = 1), [1, 2](sum = 3), [2](sum = 2), [3](sum = 3).

    Input: A = [1, 2, 3, 4], start = 1, end = 100
    Output: 10
    Explanation: Any subarray is ok.
    """
    def subarray_sum_i_i(self, a: List[int], start: int, end: int) -> int:
        # write your code here
        # find all subarray of a list of integers
        # use list to track all sums from those subarrays
        # find and count if each_sum from the sum_dict() is in given sum array [start, end]
        
        # find all subarray of a list of integers:
        n = len(a)
        if n <=0:
            return 0
        sum_list = []

        #check if each_sum in sum_list is in the given_sum_array
        given_sum_array = range(start, end + 1)
        print("given_sum_array", given_sum_array)
        sum_dict = dict()
        for each_sum in given_sum_array:
            sum_dict[each_sum] = 0

        counter = 0

        for i in range(n):
            # i in the length of the subarray
            # new_sub_arr = []
            left, right = 0, 0 + i
            while right < n:
                
                new_sub_arr = a[left:right+1]
                sum_list = sum(new_sub_arr)
                if sum_list in given_sum_array:
                    counter += 1
                left += 1
                right = left + i
                print("left, right, new_sub_arr")
                print(left, right, new_sub_arr) 

        # print("sum_list", sum_list, len(sum_list))

        
        
        return counter


    def subarray_sum_i_i02(self, a: List[int], start: int, end: int) -> int:
        n = len(a)
        if n <= 0:
            return 0

        given_sum_array = range(start, end + 1)

        counter = 0

        for i in range(n):

            left, right = 0, 0 + i
            while right < n:
                
                new_sub_arr = a[left:right+1]
                sum_list = sum(new_sub_arr) # here could be improved
                if sum_list in given_sum_array: # here could be improved
                    counter += 1
                left += 1
                right = left + i
        return counter
    
    def subarray_sum_i_i03(self, a: List[int], start: int, end: int) -> int:
        n = len(a)
        if n <= 0:
            return 0

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + a[i]

        count = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                subarray_sum = prefix_sum[j] - prefix_sum[i]
                if start <= subarray_sum <= end:
                    count += 1

        return count

new_solution = Solution()
A = [1, 2, 3, 4, 5]
start = 3
end = 7
result = new_solution.subarray_sum_i_i03(A, start, end)

print("result", result)