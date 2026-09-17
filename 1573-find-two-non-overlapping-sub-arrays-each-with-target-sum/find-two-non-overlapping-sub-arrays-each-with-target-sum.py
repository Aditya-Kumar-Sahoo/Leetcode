class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        best = [INF] * n
        prefix = {0: -1}

        curr_sum = 0
        ans = INF
        min_length = INF

        for i in range(n):
            curr_sum += arr[i]

            if curr_sum - target in prefix:
                start = prefix[curr_sum - target]
                length = i - start

                if start >= 0 and best[start] != INF:
                    ans = min(ans, length + best[start])

                min_length = min(min_length, length)

            best[i] = min_length
            prefix[curr_sum] = i

        return -1 if ans == INF else ans