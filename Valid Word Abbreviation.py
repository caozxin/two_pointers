class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        test_word = '55'
        # print("test", test_word.isdigit())
        print("max_i, max_j", len(word), len(abbr))


        if len(word) < len(abbr):
            return False

        i, j = 0, 0

        while j < len(abbr) and i < len(word):
            # print(abbr[j])
            step = 1
            if abbr[j].isdigit():
                if abbr[j] == '0': # any leading zero we return False
                    return False

                while abbr[j:j + step].isdigit() and step < len(abbr) : # here we could change it for abbr[j + step].isdigit()
                    step += 1
                i_steps = int(abbr[j:j + step-1])
                print("j+step", int(abbr[j:j + step-1]), i_steps)
                i += i_steps 
                print("i, j", i, j)

                j = j + step - 1 # we park j for now
                if j >= len(abbr) or i >= len(word):
                    return False
                print("i, j", i, j, word[i], abbr[j])

            print("i, j", i, j, word[i], abbr[j])
            if word[i] != abbr[j]:
                return False
            # print(i, j)
            j += 1
            i += 1

        return True
