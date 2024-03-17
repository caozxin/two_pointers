class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def is_valid_parentheses(self, s: str) -> bool:
        # write your code here
        if not s:
            return

        matching_dict = {"(":")", "[":"]", "{":"}"}

        fast, slow = 0, 0 

        n = len(s)

        if n % 2 == 1: # it means odd number of items
            return False

        for slow in range (len(s)):

            if matching_dict.get(s[slow]): # it finds the first half of any qualified parentheses
                print("matching", s[slow])
                fast = slow + 1

                while fast < len(s) and fast > slow:

                    if s[fast] !=  matching_dict.get(s[slow]):
                        # print("find it", s[fast])
                        print("not pairng")
                        # return False
                    fast += 1

        # return True

            
