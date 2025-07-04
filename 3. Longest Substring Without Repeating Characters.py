from collections import Counter
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0
        left = 0
        window_count = Counter(s)
        # print(window_count)
        for each in window_count:
            # print(each)
            window_count[each] = 0
        # print(window_count)
        for right in range(len(s)):
            window_count[s[right]] += 1
            # print(window_count)
            while window_count[s[right]] > 1:
                window_count[s[left]] -= 1 
                left += 1
            max_len = max(max_len, right + 1 - left)
            # print(max_len, s[left:right+1])
        # exit()

        return max_len

