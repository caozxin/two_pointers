class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return 

        mapping = { "(": ")", "[": "]", "{":"}"}
        # print(mapping)
        target = []

        for each in s:
            if each in mapping.keys():
                # print(each, mapping[each])
                target.append(mapping[each])
            elif len(target) != 0 and each == target.pop():
                continue
                # print("matching", each)
                # return True
            else:
                return False

        return len(target) == 0

  """
  Note: use stack to pop the expected matching closed brackets; order matters. 
  """
