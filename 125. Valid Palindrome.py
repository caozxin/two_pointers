class Solution:
    def isPalindrome(self, s: str) -> bool:
        #none handling:
        if not s or len(s) == 0:
            return False

        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():  # Note 1, 2
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():  # handel the False case first
                return False
            l += 1
            r -= 1
        return True

