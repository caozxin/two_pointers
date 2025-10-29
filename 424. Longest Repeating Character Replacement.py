from typing import List
# from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_count = float('-inf')
        print(n)
        
        for left in range(n):
            right = -1 # right and left start at the same place
            print("left, right", left, right)
            curr_count = 1
            max_replacement = k 

            while right < n - 1 and max_replacement >= 0:
                right += 1
                print(" ", left, right, s[left], s[right], curr_count)
                #now we compare s[left] and s[left+1]
                if right != left and s[right] != s[left] and max_replacement > 0:
                    #we use replacement if k > 0 
                    # right += 1
                    max_replacement -= 1
                    curr_count += 1
                elif right != left and s[right] == s[left] :
                    # if s[left] and s[left+1] are matching, just update curr_count
                    curr_count += 1
                elif right == left:
                    continue
                else:
                    #if s[left] and s[left+1] are not matching and max_replacement <= 0
                    break

            print(left, right, curr_count)
            if curr_count >= max_count:
                max_count = curr_count
                print("max", max_count)
            # exit()
        return max_count
