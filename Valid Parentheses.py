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

        if n == 1:
            return False

        while fast < len(s):
            print("b4", slow, fast)
            if slow == fast:
                print("1", slow, fast)
                pass
            else:
                if matching_dict.get(s[slow]) == s[fast]:
                    print("2", slow, fast)
                    pass 
                else:
                    print("3", slow, fast)
                    return False
            fast +=1
        
        return True
