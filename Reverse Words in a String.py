#Reverse Words in a String
#first version: using Python built-in functions
class Solution:
    def reverseWords(self, s: str) -> str:
        #first version:
        res = s.split(' ')
        # print(res)

        post_res = []
        for each in res:
            if each:
                post_res.append(each)
        # print(post_res)
        # print(reversed(res))
        final_res = None
        final_res = ' '.join(reversed(post_res))
        # print(final_res)
        return final_res
