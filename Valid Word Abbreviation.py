class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(word) < len(abbr):
            return False

        i, j = 0, 0

        while j < len(abbr) and i < len(word):
            step = 1
            if abbr[j].isdigit():
                if abbr[j] == '0': # any leading zero we return False
                    return False

                while abbr[j:j + step].isdigit() and step < len(abbr) : # here we could change it for abbr[j + step].isdigit()
                    step += 1
                i_steps = int(abbr[j:j + step-1])

                i += i_steps 

                j = j + step - 1 # we park j for now
                if j >= len(abbr) or i >= len(word):
                    return False
                    
            if word[i] != abbr[j]:
                return False

            j += 1
            i += 1

        return True
