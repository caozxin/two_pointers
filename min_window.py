#32 · Minimum Window Substring
# Given two strings source and target. Return the minimum substring of source which contains each char of target.
class Final_Solution:
    def min_window(self, source: str, target: str) -> str:
        target_count = {}
        for char in target:
            target_count[char] = target_count.get(char, 0) + 1

        required_chars = len(target_count)
        formed_chars = 0
        left, right = 0, 0
        current_window = {}

        min_length = float('inf')
        min_window = ""

        while right < len(source):
            char = source[right]
            current_window[char] = current_window.get(char, 0) + 1

            if char in target_count and current_window[char] == target_count[char]:
                formed_chars += 1

            while formed_chars == required_chars:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = source[left:right + 1]

                left_char = source[left]
                current_window[left_char] -= 1

                if left_char in target_count and current_window[left_char] < target_count[left_char]:
                    formed_chars -= 1

                left += 1

            right += 1

        return min_window

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
