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


# my better version:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum()
        #none handling:
        if not s:
            return True

        n = len(s)
        left, right = 0, n -1 
        s.replace(" ", '')
        s = s.lower()
        while left < right:
            # print(left, right, s[left], s[right])
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1

            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
