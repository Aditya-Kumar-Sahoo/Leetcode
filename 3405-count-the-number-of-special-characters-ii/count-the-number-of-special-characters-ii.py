class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                if ch not in first_upper:
                    first_upper[ch] = i

        count = 0

        for ch in last_lower:
            upper = ch.upper()

            if upper in first_upper:
                if last_lower[ch] < first_upper[upper]:
                    count += 1

        return count