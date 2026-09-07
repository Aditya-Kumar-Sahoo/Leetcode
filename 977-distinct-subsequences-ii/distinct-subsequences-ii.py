class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26
        total = 0

        for ch in s:
            i = ord(ch) - ord('a')

            new = total + 1

            total = total - dp[i] + new
            dp[i] = new

            total %= MOD

        return total