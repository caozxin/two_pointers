class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome

    description: Given a string, determine if it is a palindrome, only letters and numbers are considered and case is ignored

    Input: "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama"

    Input: "race a car"
    Output: false
    Explanation: "raceacar"

    输入: "1b , 1"
    输出: true
    解释: "1b1"

    """
    def is_palindrome(self, s: str) -> bool:
        # write your code here
        initial_string = s
        print("initial_string", initial_string)

        #add pre-processing:
        spec_char = [",", ".", ":", "!", ";", "(", ")"]
        modified_string = initial_string.replace(" " , "")
        modified_string = modified_string.lower()
        for each_spec_char in spec_char:
            modified_string = modified_string.replace(each_spec_char, "")
        print("modified_string", modified_string, len(modified_string))

        m = len(modified_string)
        left, right = 0, m - 1

        while left <= right:
            if modified_string[left] == modified_string[right]:
                left +=1
                right -= 1
            elif modified_string[left] != modified_string[right]:
                return False
            
            if left == right:
                break
        return True



new_solution = Solution()
s = "A man, a plan, a canal: Panama" #return True
s02 = "race a car" #return False
s03 = "1b , 1" #return True

# samples = [s, s02, s03]
# for each_sample in samples:
#     result = new_solution.valid_palindrome(each_sample)
#     print("result", result)

result = new_solution.is_palindrome(s03)
print("result", result)