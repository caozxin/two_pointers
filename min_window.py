#32 · Minimum Window Substring
# Given two strings source and target. Return the minimum substring of source which contains each char of target.

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def min_window(self, source: str, target: str) -> str:
        # write your code here
        print(source, target)
        def check_matching_target(curr_window:str, target:str) -> bool:
            # print("curr_window, target")
            # print(curr_window, target)
            if curr_window == target:
                return True
            
            for j in range(len(curr_window)):
                if curr_window[j] in target:
                    target = target.replace(curr_window[j], "", 1)
            # print(curr_window, target)
            # exit()
            if len(target) == 0:
                return True
            else:
                return False

        if not source or not target:
            return ""
        min_window = ""
        if len(source) < len(target):
            return ""

        n = len(source)
        k = len(target) # any qualified min_window should have size >= k
        while k < n + 1: # k = size of the substring
            for right in range(k, n+1):
                left = right - k
                curr_window = source[left:right]

                #def check_matching_target(curr_window, target)
                if check_matching_target(curr_window, target):# when len(curr_window) > k:
                    # curr_window = source[left:right]
                    min_window = curr_window
                    # print("min_window", curr_window)
                    return min_window
            k += 1

            # exit()
            
        # exit()

        return min_window
