
import sys
from math import comb

sys.setrecursionlimit(10000)

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            ways = comb(len(arr) - 1, len(left))
            ways *= solve(left)
            ways *= solve(right)

            return ways % MOD

        return (solve(nums) - 1) % MOD
