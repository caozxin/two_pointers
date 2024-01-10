#Given a string original and a string check, find the starting index of all substrings of original that is an anagram of check. The output must be sorted in ascending order.

from typing import List

def find_all_anagrams(original: str, check: str) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    def pass_check(window: str, check: str) -> bool:
#         print("window, check")
#         print(window, check)
        for i in range(len(window)):
            if window[i] in check:
                check = check.replace(window[i],"", 1)
        if len(check) == 0:
            return True
        else:
            return False
    
    if not original: 
        return []
    result_list = [] # list out global variable
    n = len(original)
    k = len(check) # this is the fixed window size
    window = original[:k] # initiate the window
#     print('window', window)

    for right in range(k, n+1):
        left = right - k
        curr_check = check
        window = original[left:right]
#         print("curr_check", curr_check, window)

        if pass_check(window, check):
#             print("pass")
            result_list.append(left)

    return result_list
