class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = [0] * n

        i = 0

        while i < n:
            j = i + 1

            # Find all values belonging to the same group
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Original indices of this group
            indices = sorted(arr[k][1] for k in range(i, j))

            # Values are already sorted
            values = [arr[k][0] for k in range(i, j)]

            # Put smallest values at smallest indices
            for idx, value in zip(indices, values):
                ans[idx] = value

            i = j

        return ans
    