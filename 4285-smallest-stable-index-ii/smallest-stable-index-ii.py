class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        right = [0] * n
        right[n - 1] = nums[n - 1]

        # Suffix minimum
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        # Prefix maximum + check
        left = 0

        for i in range(n):
            left = max(left, nums[i])

            if left - right[i] <= k:
                return i

        return -1