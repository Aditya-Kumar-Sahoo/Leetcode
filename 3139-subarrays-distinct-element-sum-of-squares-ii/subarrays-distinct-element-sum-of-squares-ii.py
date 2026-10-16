
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1

                # (x + 1)^2 = x^2 + 2*x + 1
                sum2[node] = (
                    sum2[node] + 2 * sum1[node] + length
                ) % MOD

                sum1[node] = (sum1[node] + length) % MOD
                lazy[node] += 1
                return

            mid = (start + end) // 2

            if lazy[node]:
                val = lazy[node]
                for child, l, r in (
                    (node * 2, start, mid),
                    (node * 2 + 1, mid + 1, end)
                ):
                    length = r - l + 1
                    sum2[child] = (
                        sum2[child] + 2 * val * sum1[child]
                        + val * val * length
                    ) % MOD
                    sum1[child] = (
                        sum1[child] + val * length
                    ) % MOD
                    lazy[child] += val

                lazy[node] = 0

            if left <= mid:
                update(node * 2, start, mid, left, right)

            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            sum1[node] = (
                sum1[node * 2] + sum1[node * 2 + 1]
            ) % MOD

            sum2[node] = (
                sum2[node * 2] + sum2[node * 2 + 1]
            ) % MOD

        last_seen = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            ans = (ans + sum2[1]) % MOD
            last_seen[x] = i

        return ans
