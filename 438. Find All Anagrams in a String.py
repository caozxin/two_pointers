class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #none handling:
        if not s or not p:
            return []
        result = []
        def check_anagram(input_s, ang_p):

            for each in input_s:
                if each not in ang_p:
                    return False
                # print(each)
                ang_p = ang_p.replace(each, "", 1) # we need to update the ang_p after replaceing it. Only replace 1 char at once. 
            # print(ang_p)
            return len(ang_p) == 0

        # print(check_anagram("abe", "ba"))

        for right in range(len(p), len(s)+1):
            left = right - len(p)
            # print(left, right, s[left:right])
            window =  s[left:right]
            # print(left, right, window)
            # print(check_anagram(window, p))
            if check_anagram(window, p):
                result.append(left)
        return result


