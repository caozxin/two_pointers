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


