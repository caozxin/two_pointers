class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        # this question cannot sort()

        if not s or k  == 0:
            return 0

        num_of_unique_chars = 0

        n = len(s)

        slow, fast = 0, 1

        for slow in range(n):
            print("slow", slow)

            fast = slow + 1
            while fast < n and s[slow] == s[fast]: # only continuous dups do not count toward k
                print("dup fast", fast)
                fast += 1

            print("fast", fast)
            k -=1 
            print("remaining k", k)

            if fast >= n:
                break

            if k <= 0:
                # print(s[:slow])
                break

        return max(slow+1, fast)
    
    def length_of_longest_substring_k_distinct_default(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0

        num_of_unique_chars = 0
        char_count = {}  # to store the count of each character

        n = len(s)
        slow, fast = 0, 0
        max_length = 0

        while fast < n:
            if s[fast] not in char_count or char_count[s[fast]] == 0:
                num_of_unique_chars += 1

            char_count[s[fast]] = char_count.get(s[fast], 0) + 1 # we are updating the counter char_count when we find dups

            while num_of_unique_chars > k:
                char_count[s[slow]] -= 1
                if char_count[s[slow]] == 0:
                    num_of_unique_chars -= 1
                slow += 1

            max_length = max(max_length, fast - slow + 1)
            fast += 1

        return max_length
