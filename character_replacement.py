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
            # curr_len = right - left + 1

            while input_string[right] != input_string[left] and k > 0:
                print("     not matching", left, right, k)
                right += 1
                k -= 1
                print("     after", left, right, k) 
            curr_len =  right
            max_len = max(curr_len, max_len)
            print("curr_len, max_len")
            print(curr_len, max_len)
            
            
            
        exit()

        
