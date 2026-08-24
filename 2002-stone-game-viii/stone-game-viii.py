from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = list(accumulate(stones))

        f = prefix[-1]

        for i in range(len(stones) - 2, 0, -1):
            f = max(f, prefix[i] - f)

        return f