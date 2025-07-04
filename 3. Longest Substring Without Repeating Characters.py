from collections import Counter, defaultdict
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0
        left = 0
        window_count = defaultdict(int) # we need to use this to avoid non-key error

        for right in range(len(s)):
            window_count[s[right]] += 1

            while window_count[s[right]] > 1:
                window_count[s[left]] -= 1 
                left += 1
            max_len = max(max_len, right + 1 - left)


        return max_len

