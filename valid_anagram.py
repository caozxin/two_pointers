#Write a method anagram(s,t) to decide if two strings are anagrams or not.
#Two strings are anagram if they can be the same after change the order of characters

class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s: str, t: str) -> bool:
        # write your code here
        if not s or not t:
            return False
        input_string1 = s
        input_string2 = t
        #size check
        if len(input_string1) != len(input_string2):
            return False
        #chars check
        n = len(input_string1)
        # print(n)
        for i in range(n):
            if input_string1[i] in input_string2:
                input_string2 = input_string2.replace(input_string1[i], "", 1) # replace it only once
        # print(input_string1, input_string2)
        if len(input_string2) != 0:
            return False
        return True
        
