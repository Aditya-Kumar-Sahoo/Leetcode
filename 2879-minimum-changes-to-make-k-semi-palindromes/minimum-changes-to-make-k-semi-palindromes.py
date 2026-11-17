class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        # Precompute semi-palindrome conversion costs
        for l in range(n):
            for r in range(l + 1, n):
                length = r - l + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for offset in range(d):
                        left = l + offset
                        right = l + offset + ((length - 1 - offset) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[l][r] = min(cost[l][r], changes)

        # DP
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for t in range(1, k + 1):
            for i in range(2 * t, n + 1):
                for j in range(2 * (t - 1), i - 1):
                    dp[t][i] = min(
                        dp[t][i],
                        dp[t - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]