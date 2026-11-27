from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        if n == 0 or budget <= 0:
            return 0

        factors = [f for f, _ in items]
        prices = [p for _, p in items]
        pmin = min(prices)

        # value of the first purchase of item i: the copy itself + free copies it triggers
        values = []
        for i in range(n):
            fi = factors[i]
            free = 0
            for j in range(n):
                if j != i and factors[j] % fi == 0:
                    free += 1
            values.append(1 + free)

        # 0/1 knapsack: dp[b] = max copies from first purchases using at most b
        dp = [0] * (budget + 1)
        for i in range(n):
            w, v = prices[i], values[i]
            if w > budget:
                continue
            for b in range(budget, w - 1, -1):
                cand = dp[b - w] + v
                if cand > dp[b]:
                    dp[b] = cand

        # spend whatever is left on extra copies of the cheapest item
        best = 0
        for b in range(budget + 1):
            total = dp[b] + (budget - b) // pmin
            if total > best:
                best = total
        return best