# my version:
class Solution:
    # my version:
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
# improved version:        
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # Pointers for word and abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':  # Leading zero case, invalid
                    return False

                # Capture the number part of the abbreviation
                start = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                num = int(abbr[start:j])  # Extract number from substring
                i += num  # Skip 'num' characters in the word
                
                # If `i` goes out of bounds, return False
                if i > len(word):
                    return False

            else:
                # Compare the current character in word and abbr
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        # Both i and j should reach the end simultaneously
        return i == len(word) and j == len(abbr)
