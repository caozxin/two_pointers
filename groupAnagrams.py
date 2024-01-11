# 49. Group Anagrams
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # print(strs)

        def generate_each_check(a_string: str) -> str:
            # print(a_string)

            check = []
            result_check = ""
            for each_char in a_string:
                check.append(each_char)
            check.sort() # sort the check
            # print(check)
            for each in check:
                result_check += each
            return result_check

        if not strs:
            return []

        letters_dict = {}
        result_list = []

        for each_string in strs:
            curr_check = generate_each_check(each_string)
            # print("curr_check", curr_check)
            if curr_check in list(letters_dict.keys()):
                # print(True) #if curr_check in letters_dict{}
                letters_dict[curr_check].append(each_string)
            else:
                # print(False) # if curr_check does not exist in letters_dict{} yet
                letters_dict[curr_check] = [each_string]
                
            # print(letters_dict)
        
        for each in list(letters_dict.values()):
            # print(each)
            result_list.append(each)

        return result_list
