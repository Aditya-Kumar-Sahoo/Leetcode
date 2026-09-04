class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # suffix minimum
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        # prefix maximum + check
        leftMax = 0

        for i in range(n):
            leftMax = max(leftMax, nums[i])

            if leftMax - right[i] <= k:
                return i

        return -1