class Solution:
    def reverseWords(self, s: str) -> str:
        # #first version with python built-in
        # res = s.split(' ')
        # # print(res)

        # post_res = []
        # for each in res:
        #     if each:
        #         post_res.append(each)
        # # print(post_res)
        # # print(reversed(res))
        # final_res = None
        # final_res = ' '.join(reversed(post_res))
        # # print(final_res)
        # return final_res

        # #second version with Two Pointers
        if not s:
            return

        start, end = 0, 0
        # print(len(s))
        # print(s[end:end+1])
        
        # print(start, end, s[start:end])
        res = []
        for i in range(len(s)):
            if s[i:i+1] == ' ':
                # print(s[i:i+1])
                # print(s[start:end].strip())
                if s[start:end]: 
                    res.append(s[start:end])
                # print(res)
                end += 1
                start = end
                # break
            else:
                end += 1
        if s[start:end]: 
            res.append(s[start:end])
        # print(res)

        final_res = ' '.join(reversed(res))
        # print(final_res)
        return final_res

