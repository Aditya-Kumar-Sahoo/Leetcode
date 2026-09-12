from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((r, l, w, i))

        arr.sort()

        ends = [x[0] for x in arr]

        dp = [[(-1, []) for _ in range(5)] for _ in range(n + 1)]
        dp[0][0] = (0, [])

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] < b[1] else b

        for i in range(1, n + 1):
            r, l, w, idx = arr[i - 1]

            p = bisect_left(ends, l, 0, i - 1)

            for k in range(5):
                dp[i][k] = dp[i - 1][k]

                if k > 0 and dp[p][k - 1][0] != -1:
                    score, indices = dp[p][k - 1]

                    candidate = (
                        score + w,
                        sorted(indices + [idx])
                    )

                    dp[i][k] = better(dp[i][k], candidate)

        ans = dp[n][0]

        for k in range(1, 5):
            ans = better(ans, dp[n][k])

        return ans[1]