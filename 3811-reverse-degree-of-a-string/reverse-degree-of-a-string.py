class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, c in enumerate(s):
            reverse_position = 26 - (ord(c) - ord('a'))
            ans += (i + 1) * reverse_position

        return ans