
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(arr)}
        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
