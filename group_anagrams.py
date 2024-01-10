#Given a string original and a string check, find the starting index of all substrings of original that is an anagram of check. The output must be sorted in ascending order.

from typing import List

def find_all_anagrams(original: str, check: str) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    if not original: 
        return []
    result_list = [] # list out global variable
    n = len(original)
    for i in range(n):
        curr_check = check
        print("curr_check", curr_check)
        if original[i] in curr_check:
            
            curr_idx = i
            curr_char = original[curr_idx]
            curr_check = curr_check.replace(curr_char,"")
            print(curr_idx, curr_char, curr_check, len(curr_check))
            next_idx = i + 1
            while next_idx < n and len(curr_check) > 0: 
                next_char = original[next_idx]
                if next_char in curr_check:
                    curr_check = curr_check.replace(next_char,"")
                    print(next_idx, next_char, curr_check, len(curr_check))
                    
                next_idx += 1
                if len(curr_check) == 0:
                    result_list.append(curr_idx)
                    print("result_list", result_list)
#                     exit()
                    break
    return result_list
