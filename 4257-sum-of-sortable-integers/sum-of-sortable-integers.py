
class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        # Prefix maximums
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        # Suffix minimums
        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        # Count ordinary adjacent descents
        desc = [0] * n
        for i in range(n - 1):
            desc[i + 1] = desc[i] + (nums[i] > nums[i + 1])

        ans = 0

        # Check every divisor of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for l in range(0, n, k):
                r = l + k - 1

                # Count descents, including the circular edge
                drops = desc[r] - desc[l]
                drops += nums[r] > nums[l]

                if drops > 1:
                    valid = False
                    break

                # Ensure elements in earlier blocks
                # do not exceed elements in later blocks
                if pref_max[l] > suff_min[l]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
