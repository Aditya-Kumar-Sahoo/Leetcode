class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        li = []
        for i in word:
            if i not in li and i.lower() in word and i.upper() in word:
                count += 1
            if i == i.lower():
                li.append(i)
                li.append(i.upper())
            else:
                li.append(i)
                li.append(i.lower())
        return count