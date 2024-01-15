# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    """
    @param s: a string
    @return: an integer
    example = abcabcbb -->3,  The longest substring is "abc".
    example = bbbbb -->1,  The longest substring is "b".
    """
    def length_of_longest_substring(self, s: str) -> int:
        # write your code here
        if not s:
            return 0

        left, right = 0, 0
        n = len(s)
        longest_len = 0

        for right in range(n):
            
            right += 1

            while s[left] == s[right] and left < n:
                left += 1
            print("left, right", left, right)
            curr_len = right - left + 1
            print("curr_len", curr_len)
            longest_len = max(longest_len, curr_len)
            print("longest_len", longest_len)
