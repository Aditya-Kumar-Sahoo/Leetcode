from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        cnt = [0] * (n + 1)
        for f, _ in items:
            cnt[f] += 1

        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            s = 0
            for m in range(f, n + 1, f):
                s += cnt[m]
            multiples[f] = s

        pmin = min(p for _, p in items)

        groups = []
        for f, p in items:
            free = multiples[f] - 1
            if free > 0:
                groups.append((p, free))
        groups.sort()

        best = budget // pmin
        a = 0
        cost = 0
        for p, c in groups:
            if p >= 2 * pmin:   
                break
            k = min(c, (budget - cost) // p)
            if k <= 0:
                break
            cost += k * p
            a += k
            total = 2 * a + (budget - cost) // pmin
            if total > best:
                best = total
            if k < c:           
                break
        return best