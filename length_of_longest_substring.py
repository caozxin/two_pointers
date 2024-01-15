# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    """
    @param s: a string
    @return: an integer
    example = abcabcbb -->3,  The longest substring is "abc".
    example = bbbbb -->1,  The longest substring is "b".
    """
    def length_of_longest_substring00(self, s: str) -> int:
        # write your code here
        if not s:
            return 0

        left, right = 0, 1
        input_string = s

        n = len(input_string)
        longest_len = 0

        for right in range(1, n):
            
            # the window here is substring with non-repeating characters!
            window = input_string[left:right]
            print("left, right", left, right)
            # print("window", window)
            #1st check on outside dups:
            while input_string[left] == input_string[right] and left < n:
                print(" *outside has dups")
                left += 1
                # print(left, right, window)
            
            #2) check on inside dups:
            while input_string[right] in input_string[left:right] and input_string[left] != input_string[right] and left < n:
                print(" *inside has dups")
                left += 1

            # print("left, right", left, right)
            curr_len = right - left + 1
            print("curr_len", curr_len)
            longest_len = max(longest_len, curr_len)
            print("longest_len", longest_len)
        # exit()
        return longest_len


    def length_of_longest_substring(self, s: str) -> int:
        if not s:
            return 0

        left, right = 0, 0  # Initialize both pointers at the beginning of the string
        n = len(s)
        longest_len = 0
        unqiue_char_set = set()  # Use a set to keep track of unique characters in the current window

        while right < n:
            if s[right] not in unqiue_char_set:
                unqiue_char_set.add(s[right])
                right += 1
                longest_len = max(longest_len, right - left)
            else:
                unqiue_char_set.remove(s[left])
                left += 1

        return longest_len

        # for right in range(n):
        #     if right < n  and s[right] not in unqiue_char_set:
        #         unqiue_char_set.add(s[right])
        #         longest_len = max(longest_len, right - left)
        #     elif right < n and s[right] in unqiue_char_set: # if s[right] is in unqiue_char_set() already, then it is no longer unique. 
        #         unqiue_char_set.remove(s[left])
        #         left += 1
            
        # return longest_len

