class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def is_valid_parentheses(self, s: str) -> bool:
        # write your code here
        if not s:
            return

        n = len(s)

        if n % 2 == 1: # it means odd number of items
            return False

        matching_dict = {"(":")", "[":"]", "{":"}"}
        stack = []

        for pointer in range (len(s)):

            if matching_dict.get(s[pointer]): # it finds the first half of any qualified parentheses
                # print("matching", s[slow])
                stack.append(s[pointer]) # only append to stack when it is first half
            else:
                if not stack:
                    return False # when stack has no any first half
                expected = stack.pop()
                if s[pointer] != matching_dict[expected]: # if last first half in stack does not matching it
                    return False

        if not stack:
            return True
        else:
            return False

            
