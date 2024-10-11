class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check(input_s: str)-> bool:
            print("input_s", input_s)
            i, j = 0, len(input_s)-1,
            while i < len(input_s) and j >= 0:
                print("i, j", i, j)
                if input_s[i] != input_s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        start, end = 0, len(s) - 1

        while start < len(s) and end >= 0:
            print("b4", start, end)
            if s[start] != s[end]:
                print("not matching", start, end)
                
                if check(s.replace(s[start], '')) or check(s.replace(s[end], '')):
                    return True
                else:
                    return False

            start += 1
            end -= 1
            print("af", start, end)

        return True
