class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # Helper function to check if a substring is a palindrome
        def check_palindrome(s: str, left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # Two pointers approach to check the main string
        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                # Try skipping either the left character or the right character
                # and check if it results in a valid palindrome
                return check_palindrome(s, start + 1, end) or check_palindrome(s, start, end - 1)
            start += 1
            end -= 1

        return True  # If no mismatches found, it's already a palindrome

# # Test case
# sol = Solution()
# print(sol.validPalindrome("abca"))  # Expected: True
