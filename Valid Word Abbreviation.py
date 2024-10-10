class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        test_word = '55'
        # print("test", test_word.isdigit())


        if len(word) < len(abbr):
            return False

        i, j = 0, 0

        while j < len(abbr):
            # print(abbr[j])
            step = 1
            if abbr[j].isdigit():

                while abbr[j:j + step].isdigit():
                    step += 1

                print("j+step", abbr[j:j + step-1])
                j = j + step - 1

            # exit()
            if word[i] != word[j]:
                return False

            j += 1
            i += 1
            
            # return False
