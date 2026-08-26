class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""
        min_len = float("inf")

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # Too many ones
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Remove unnecessary leading zeroes
            while ones == k and s[left] == '0':
                left += 1

            # Current window has exactly k ones
            if ones == k:
                curr = s[left:right + 1]

                if len(curr) < min_len or (
                    len(curr) == min_len and curr < ans
                ):
                    ans = curr
                    min_len = len(curr)

        return ans