# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.
class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def character_replacement(self, s: str, k: int) -> int:
        # write your code here
        if not s:
            return 0

        #global variables:
        input_string = s
        n = len(input_string)
        #this question is to find window with maximum repeating characters!
        left, right = 0, 0
        max_len = 0
        curr_len = 0 

        for right in range(n):
            # if matching:
            # print("     before", left, right, k) 

            if input_string[right] == input_string[left]:
                continue
            

            if right < n : 
                while k > 0 and left <= n and right + k < n:# if not matching and could be replaced
                    print("     not matching", left, right, k)
                    print(input_string[left], input_string[right])

                    right += 1
                    k -= 1
                
                left += 1
            # print("     after", left, right, k) 
            
            curr_len =  right - left + 1
            max_len = max(curr_len, max_len)
            # print("curr_len, max_len")
            # print(curr_len, max_len)
            # exit()

        return max_len

        

        """
                Certainly! Let's analyze the corrected implementation:
        
        1. **Initialization:**
           - `input_string` is assigned the input string `s`.
           - `n` is the length of the input string.
           - `left` and `right` are initialized to 0.
           - `max_len` is initialized to 0.
           - `max_repeat_count` is used to keep track of the maximum count of repeating characters in the current window.
           - `char_count` is a dictionary to store the count of each character in the window.
        
        2. **Sliding Window Approach:**
           - The algorithm uses a sliding window approach where `left` and `right` define the window boundaries.
           - `right` is iterated over the input string.
           - `char_count` is updated to keep track of the count of each character in the current window.
           - `max_repeat_count` is updated to be the maximum count of any character in the current window.
        
        3. **Adjusting the Window:**
           - If the length of the current window minus `max_repeat_count` exceeds the allowed replacements `k`, then we need to adjust the window.
           - `char_count` is updated by decrementing the count of the character at the `left` pointer.
           - `left` is incremented to shrink the window.
        
        4. **Updating Maximum Length:**
           - The maximum length of the valid substring is updated whenever the window is expanded.
           - `max_len` is the maximum length encountered so far.
        
        5. **Result:**
           - The final result is the maximum length of a substring containing all repeating letters with at most `k` replacements.
        
        The corrected implementation addresses the issues in the initial code, and it correctly handles cases where replacements are needed to maximize the length of the substring. The sliding window approach efficiently manages the window boundaries and updates the character counts as needed.
        """
